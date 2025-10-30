### 🧭 **Overall Project Sequence**

#### **1. Review Project Materials**

- Read the **Project One Guidelines and Rubric** carefully.
    
- Open and study the **Pet BAG Specification Document** — pay close attention to:
    
    - The **UML class diagram** (shows Pet class attributes and methods).
        
    - The **Functionality section** (explains check-in and check-out processes).
        
- Note your deliverables: `Pet.java`, pseudocode, flowchart, and short OOP explanation.
    

---

#### **2. Set Up Your Java Environment in Codio**

- Launch your **Codio virtual lab** for IT-145.
    
- Verify that your workspace supports Java compilation (`javac`, `java`).
    
- Create a new file named **`Pet.java`** in your workspace.
    

---

#### **3. Implement the `Pet.java` Class**

Follow the UML and specification closely:

1. **Define attributes** for:
    
    - `petType`, `petName`, `petAge`, `dogSpaces`, `catSpaces`, `daysStay`, `amountDue`.  
        _(Choose appropriate data types — likely `String`, `int`, and `double`.)_
        
2. **Create at least one constructor**
    
    - _Minimum requirement:_ default constructor.
        
    - _To exceed expectations:_ initialize all attributes in the constructor.
        
3. **Write accessors and mutators** (getters/setters) for each attribute.
    
    - Example:
        
        `public String getPetName() { return petName; } public void setPetName(String petName) { this.petName = petName; }`
        
4. **Add inline comments** explaining each section and method.
    

You don’t connect this to other classes or run it yet — you’re just building the class structure.

---

#### **4. Write Pseudocode for One Method**

- Choose **either** the _pet check-in_ or _pet check-out_ process described in the specification.
    
- Keep pseudocode _high-level and organized_, no more than one page.
    
- Focus on logical flow (inputs → decisions → outputs).  
    Example structure:
    
    `START Prompt user for pet name and type Assign available space (dog or cat) Set days of stay Calculate amount due Display confirmation END`
    

---

#### **5. Create a Flowchart**

- Convert that pseudocode into a **flowchart** (hand-drawn or digital).
    
- Include:
    
    - **Start / End** ovals
        
    - **Rectangles** for process steps
        
    - **Diamonds** for decision points (e.g., “Dog or Cat?”)
        
    - **Arrows** for flow direction
        

The chart must fit on one page and visually mirror your pseudocode’s logic.

---

#### **6. Write OOP Explanation Paragraph**

In your **Global Rain Summary Report**, include a short paragraph (4–6 sentences) describing:

- How your class design demonstrates **object-oriented programming principles**, such as:
    
    - **Encapsulation** (private attributes, getters/setters)
        
    - **Inheritance** (Pet could later extend or be extended by other classes)
        
    - **Abstraction** (defining essential pet properties, hiding details)
        
- Example:
    
    > “In this project, I applied encapsulation by declaring all class fields private and creating public getters and setters for controlled access. The class structure supports inheritance for future subclasses such as Dog or Cat. This design encourages modularity, code reuse, and maintainability, aligning with OOP principles.”
    

---

#### **7. Assemble the Global Rain Summary Report**

- Insert into the provided Word template:
    
    - Your **pseudocode**
        
    - Your **flowchart** (as image or embedded diagram)
        
    - Your **OOP explanation paragraph**
        

---

#### **8. Submit to Brightspace**

- Upload:
    
    1. `Pet.java`
        
    2. Your **Global Rain Summary Report (.docx or .pdf)**
        
- Verify submission and file extensions (`.java`, not `.class`).
    

---

### ✅ **Summary of Deliverables and Order**

|Step|Deliverable|File Name / Format|
|---|---|---|
|1|Read rubric & specification|—|
|2|Configure environment|—|
|3|Java class implementation|`Pet.java`|
|4|Pseudocode for one method|Inside Summary Report|
|5|Flowchart (check-in or check-out)|Embedded image|
|6|OOP explanation|Summary Report paragraph|
|7|Final submission|Brightspace upload|

