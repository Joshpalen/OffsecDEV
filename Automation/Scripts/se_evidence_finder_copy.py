#!/usr/bin/env python3
"""
SE Evidence Finder (COPY MODE)
Copies (does not move) and normalizes social-engineering evidence into a Reports/<campaign>/Evidence/ folder.

Usage:
    python se_evidence_finder_copy.py --src /path/to/raw_evidence --campaign CAMPAIGN_NAME --vault /path/to/vault

What it does:
- Scans src directory recursively for common evidence files (images, pcap, txt, eml, csv, mp3).
- Normalizes filenames to: YYYYMMDD_HHMMSS_<type>_<shorthash>.<ext>
- Copies files into vault/Reports/<campaign>/Evidence/{images,pcap,logs,emails,attachments,audio,other}
- Generates a manifest JSON and an index Markdown (Evidence_Index.md) summarizing files and metadata
- Safe: files are copied (originals preserved). Use when you want to keep originals intact.

Requires: Python 3.8+
"""
import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime

# file type mapping
TYPE_MAP = {
    'images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'],
    'pcap': ['.pcap', '.pcapng'],
    'logs': ['.log', '.txt', '.csv'],
    'emails': ['.eml', '.msg'],
    'audio': ['.mp3', '.wav', '.m4a'],
    'attachments': ['.pdf', '.docx', '.xlsx', '.pptx', '.zip', '.rar', '.7z'],
}

def short_hash(path, length=8):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()[:length]

def detect_type(ext):
    ext = ext.lower()
    for k, v in TYPE_MAP.items():
        if ext in v:
            return k
    return 'other'

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def normalize_and_copy(src_path, dest_base, campaign):
    stat = os.stat(src_path)
    mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y%m%d_%H%M%S')
    ext = os.path.splitext(src_path)[1].lower()
    ftype = detect_type(ext)
    h = short_hash(src_path)
    filename = f"{mtime}_{ftype}_{h}{ext}"
    dest_dir = os.path.join(dest_base, 'Reports', campaign, 'Evidence', ftype)
    ensure_dir(dest_dir)
    dest_path = os.path.join(dest_dir, filename)
    # avoid overwrite
    if os.path.exists(dest_path):
        base, ext2 = os.path.splitext(filename)
        dest_path = os.path.join(dest_dir, f"{base}_dup{ext2}")
    shutil.copy2(src_path, dest_path)
    return {
        'original_path': src_path,
        'dest_path': dest_path,
        'type': ftype,
        'filename': os.path.basename(dest_path),
        'mtime': mtime,
        'size_bytes': os.path.getsize(dest_path),
        'sha256_short': h
    }

def scan_and_archive(src_root, vault_root, campaign):
    manifest = {
        'campaign': campaign,
        'scanned_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'files': []
    }
    # walk
    for root, dirs, files in os.walk(src_root):
        for fname in files:
            path = os.path.join(root, fname)
            try:
                meta = normalize_and_copy(path, vault_root, campaign)
                manifest['files'].append(meta)
                print(f"Copied: {meta['filename']} -> {meta['dest_path']}")
            except Exception as e:
                print(f"Error copying {path}: {e}")
    # write manifest and markdown index
    report_dir = os.path.join(vault_root, 'Reports', campaign)
    ensure_dir(report_dir)
    manifest_path = os.path.join(report_dir, 'evidence_manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    # create Evidence_Index.md
    md_lines = [
        f"# Evidence Index — {campaign}",
        "",
        f"Generated: {manifest['scanned_at']}",
        "",
        "| Filename | Type | Size (bytes) | MTime | SHA256_short | Path |",
        "|---|---:|---:|---|---|---|"
    ]
    for fmeta in manifest['files']:
        md_lines.append(f"| {fmeta['filename']} | {fmeta['type']} | {fmeta['size_bytes']} | {fmeta['mtime']} | {fmeta['sha256_short']} | {fmeta['dest_path']} |")
    md_path = os.path.join(report_dir, 'Evidence_Index.md')
    with open(md_path, 'w') as f:
        f.write('\n'.join(md_lines))
    print(f"Manifest written to {manifest_path}")
    print(f"Markdown index written to {md_path}")
    return manifest_path, md_path

def main():
    parser = argparse.ArgumentParser(description="SE Evidence Finder (COPY MODE) — copy and normalize evidence into vault Reports/<campaign>/Evidence/")
    parser.add_argument("--src", required=True, help="Source folder containing raw evidence")
    parser.add_argument("--campaign", required=True, help="Campaign name (used as Reports/<campaign>)")
    parser.add_argument("--vault", required=True, help="Path to your Obsidian vault root (where Reports/ will be created)")
    args = parser.parse_args()

    if not os.path.isdir(args.src):
        raise SystemExit(f"Source folder not found: {args.src}")
    if not os.path.isdir(args.vault):
        raise SystemExit(f"Vault folder not found: {args.vault}")

    print(f"Scanning {args.src} -> campaign {args.campaign} in vault {args.vault}")
    scan_and_archive(args.src, args.vault, args.campaign)

if __name__ == '__main__':
    main()
