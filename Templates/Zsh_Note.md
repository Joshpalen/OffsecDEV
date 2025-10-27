# 🐚 Zsh Note

**Date:**  
**Host / Profile:**  
**Author:**  

---

## 🎯 Objective
(Configure prompt, aliases, completion, oh-my-zsh plugin notes)

---

## ⚙️ Key Config Snippets
    # .zshrc example
    export ZSH="$HOME/.oh-my-zsh"
    ZSH_THEME="agnoster"
    plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
    source $ZSH/oh-my-zsh.sh

    # Alias
    alias ll='ls -la'

---

## 🧾 Useful Tips
- Enable autosuggestions plugin for history completion  
- Use `compdef` for custom completion  
- `bindkey` to customize keybindings

---

## 🧩 Troubleshooting
- Theme rendering issues → check `POWERLEVEL9K`/font config  
- Slow startup → profile with `zsh -xv` and disable heavy plugins

---

## 🧭 Next Steps / Notes
- Add prompt color changes  
- Standardize `.zshrc` across machines

---

**References:**  
(Oh My Zsh docs, Prezto, Zsh man page)
