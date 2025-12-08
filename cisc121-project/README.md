# CISC 121 Project: Binary Search Algorithm Visualizer

## Author
**Ennoj Haran Sukumaran**  
Queen's University Computing Student  
CISC 121 Course Project

## Live Demo
[Click here to try the Hugging Face Space](#) *(Link will be added after deployment)*

## Project Overview
This project implements a **Binary Search Algorithm Visualizer** using Python and Gradio. The application provides an interactive, step-by-step visualization of how binary search works, making it an educational tool for understanding this fundamental computer science algorithm.

## Demo Screenshots
## Demo Screenshots

### 1. Main Interface
![Main Interface](picture%201.png)
*Initial app screen with input fields and example buttons*

### 2. Algorithm in Action - Step-by-Step Search
| **Picture 2** | **Picture 2.1** |
|---------------|-----------------|
| ![Algorithm Steps Part 1](picture%202.png) | ![Algorithm Steps Part 2](picture%202.1.png) |
| *Binary search steps 1-3 finding target 7* | *Binary search steps 3-4 completing the search* |

### 3. Successful Search
![Success Result](picture%203.png)
*Target found with detailed statistics and time complexity analysis*

### 4. Edge Cases & Testing
| **Target Not Found** | **Multiple Test Examples** |
|----------------------|---------------------------|
| ![Not Found Case](picture%204.png) | ![More Examples](more examples.png) |
| *Handling case where target is not in array* | *Preloaded examples for quick testing* |

## Problem Breakdown & Computational Thinking

### Decomposition
The binary search algorithm was broken down into these components:
1. **Input Processing**: Parse and validate user input
2. **Array Preparation**: Sort input array (binary search prerequisite)
3. **Search Execution**: Iterative binary search with midpoint calculation
4. **Visualization Generation**: Create visual array representation at each step
5. **Output Display**: Present results with statistics

### Pattern Recognition
- **Divide and Conquer**: Repeatedly halves search space
- **Pointer Movement**: LOW and HIGH pointers converge toward target
- **Comparison Pattern**: Always compares middle element, eliminates half

### Abstraction
**Shown to User:**
- Visual array with indices and values
- LOW, MID, HIGH pointer positions
- Step-by-step algorithm explanation
- Comparison results and decisions
- Algorithm statistics (time/space complexity)

**Hidden from User:**
- Internal variable management
- Memory allocation details
- Error handling implementation
- GUI framework complexity

### Algorithm Design

User Input
↓
Input Validation
↓
Array Sorting
↓
Binary Search Loop
├── Calculate MID = (LOW + HIGH) // 2
├── Compare arr[MID] with target
├── If match: Return success
├── If target > arr[MID]: Search right (LOW = MID + 1)
└── If target < arr[MID]: Search left (HIGH = MID - 1)
↓
Display Results + Statistics


### Flowchart

[Start]
↓
[Get Array & Target Input]
↓
[Validate & Sort Array]
↓
[Initialize LOW=0, HIGH=len(arr)-1]
↓
╔═══════════════════════════════╗
║ while LOW <= HIGH: ║
║ MID = (LOW + HIGH) // 2 ║←┐
║ if arr[MID] == target: ║ │
║ [Return Found] → [End] ║ │
║ elif arr[MID] < target: ║ │
║ LOW = MID + 1 ║ │
║ else: ║ │
║ HIGH = MID - 1 ║ │
║ ║ │
╚═══════════════════════════════╝ │
↑ │
└──────────────────┘
↓
[Return Not Found]
↓
[End]


## Implementation Details

### Key Features
1. **Interactive Visual Interface**: Clean Gradio-based GUI with multiple display panels
2. **Step-by-Step Visualization**: Real-time array visualization with pointer tracking
3. **Educational Content**: Algorithm explanation and complexity analysis
4. **Robust Error Handling**: Graceful handling of invalid inputs
5. **Preloaded Examples**: Quick testing with one-click examples
6. **Algorithm Statistics**: Displays steps, comparisons, and complexity analysis

### Technical Specifications
- **Programming Language**: Python 3.8+
- **GUI Framework**: Gradio 4.0+
- **Algorithm**: Binary Search
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Input Format**: Comma-separated integers
- **Output**: Step-by-step visualization with statistics

## Steps to Run Locally

### Prerequisites
- Python 3.8 or higher installed
- Internet connection (for initial package installation)

### Installation
1. **Clone or download the project files**
2. **Open Command Prompt/Terminal in project folder**
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt


Running the Application
Navigate to project folder:

bash
cd cisc121-project
Run the application:

bash
python app.py
Open your browser and go to:

text
http://127.0.0.1:7860
Testing & Verification
Test Cases Executed
Normal Case: [23,5,17,42,9,31,14,8] → Target 17 → Found

Sorted Array: [1,2,3,4,5,6,7,8,9,10] → Target 7 → Found at index 6

Target at Beginning: [5,8,12,15,20] → Target 5 → Found

Target at End: [5,8,12,15,20] → Target 20 → Found

Target Not Present: [5,8,12,15,20] → Target 10 → Not Found

Empty Input: No array → Error message

Invalid Input: Letters instead of numbers → Error message

Single Element: [5] → Target 5 → Found

Large Array: 1-100 → Target 75 → Found efficiently

Testing Methodology
Functional Testing: Verified algorithm correctness

Edge Case Testing: Tested boundaries and invalid inputs

Usability Testing: Ensured intuitive interface

Performance Testing: Confirmed O(log n) time complexity

Hugging Face Deployment
Link will be added after deploying to Hugging Face Spaces

GitHub Repository
Link will be added after uploading to GitHub

Acknowledgments
Resources Used
Course Materials: CISC 121 project guidelines and lectures

Gradio Documentation: For GUI implementation guidance

Python Official Documentation: For language features and best practices

Algorithm Visualization Inspiration: USFCA algorithm visualization examples

Special Thanks
Course instructor for comprehensive project guidelines

Gradio development team for excellent UI library

Hugging Face for free deployment platform

Queen's University Computing for educational resources

Learning Outcomes
Through this project, I gained practical experience with:

Implementing search algorithms in Python

Creating interactive visualizations for educational purposes

Applying computational thinking principles

Developing user-friendly GUI applications

Comprehensive testing and documentation

Software deployment using modern platforms

Future Enhancements
Potential improvements for this project:

Add animation between steps for smoother visualization

Include sound effects for key algorithm events

Support for multiple algorithm visualizations

Export functionality for saving search sessions


Mobile-responsive design for better accessibility









