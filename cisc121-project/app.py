# app.py
# CISC 121 Project - Binary Search Algorithm Visualizer
# Student: Ennoj Haran Sukumaran
# A visual simulation of Binary Search algorithm with step-by-step explanations

import gradio as gr

def binary_search_visual(arr_str, target_str):
    """
    Perform binary search and return step-by-step visualizations and explanations.
    """
    
    # ===== INPUT VALIDATION =====
    if not arr_str or not target_str:
        return "❌ Please enter both an array and a target number.", "", "", ""
    
    # Convert array string to list
    try:
        original_arr = [int(x.strip()) for x in arr_str.split(",")]
        if len(original_arr) == 0:
            return "❌ Array cannot be empty.", "", "", ""
    except ValueError:
        return "❌ Error: Please enter numbers only, separated by commas (e.g., 5,3,9,1,7).", "", "", ""
    
    # Convert target to integer
    try:
        target = int(target_str.strip())
    except ValueError:
        return "❌ Error: Target must be a single integer number.", "", "", ""
    
    # ===== ALGORITHM INITIALIZATION =====
    arr = sorted(original_arr.copy())  # Binary search requires sorted array
    steps = []
    visual_steps = []
    comparisons = 0
    low = 0
    high = len(arr) - 1
    found = False
    position = -1
    
    # ===== INITIAL VISUALIZATION =====
    steps.append("# 🔍 **BINARY SEARCH ALGORITHM**")
    steps.append("---")
    steps.append(f"**Input Array:** {original_arr}")
    steps.append(f"**Sorted Array:** {arr}")
    steps.append(f"**Target Value:** {target}")
    steps.append("---")
    
    # Create initial array visualization
    def create_visualization(arr, low_idx, high_idx, mid_idx, found_idx=-1):
        """Create a visual representation of the current search state."""
        vis = []
        vis.append("```")
        vis.append("ARRAY INDEX:   " + "  ".join([f"{i:2}" for i in range(len(arr))]))
        vis.append("ARRAY VALUES:  " + "  ".join([f"{val:2}" for val in arr]))
        vis.append("               " + "   ".join(["──" for _ in range(len(arr))]))
        
        # Create pointer visualization
        pointers = ["   " for _ in range(len(arr))]
        
        if low_idx <= high_idx:
            # Mark search range
            for i in range(low_idx, high_idx + 1):
                pointers[i] = "░░░"
            
            # Mark middle element
            if mid_idx >= 0:
                pointers[mid_idx] = "⬆️ " if found_idx < 0 else "🎯"
            
            # Add pointer labels
            vis.append("               " + " ".join(pointers))
            vis.append("")
            
            # Add labels for LOW, MID, HIGH
            label_line = ["    " for _ in range(len(arr))]
            if low_idx < len(arr):
                label_line[low_idx] = "LOW "
            if mid_idx < len(arr) and mid_idx >= 0:
                label_line[mid_idx] = "MID "
            if high_idx < len(arr):
                label_line[high_idx] = "HIGH"
            
            vis.append("               " + " ".join(label_line))
        
        vis.append("```")
        return "\n".join(vis)
    
    # ===== BINARY SEARCH ALGORITHM =====
    step_count = 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        # Add step description
        steps.append(f"## **Step {step_count}**")
        steps.append(f"**Search Range:** Indices [{low}] to [{high}]")
        steps.append(f"**Middle Index:** mid = ({low} + {high}) // 2 = {mid}")
        steps.append(f"**Middle Value:** arr[{mid}] = {arr[mid]}")
        steps.append("")
        
        # Create visualization for this step
        current_vis = create_visualization(arr, low, high, mid)
        visual_steps.append(current_vis)
        
        # Compare middle element with target
        steps.append(f"**Comparison {comparisons}:**")
        steps.append(f"Is {arr[mid]} == {target}?")
        
        if arr[mid] == target:
            steps.append(f"✅ **MATCH FOUND!**")
            steps.append(f"The target {target} is at index {mid} in the sorted array.")
            found = True
            position = mid
            break
            
        elif arr[mid] < target:
            steps.append(f"❌ {arr[mid]} < {target}")
            steps.append(f"Target is in the **RIGHT** half.")
            steps.append(f"Update: low = mid + 1 = {mid + 1}")
            low = mid + 1
            
        else:  # arr[mid] > target
            steps.append(f"❌ {arr[mid]} > {target}")
            steps.append(f"Target is in the **LEFT** half.")
            steps.append(f"Update: high = mid - 1 = {mid - 1}")
            high = mid - 1
        
        steps.append("---")
        step_count += 1
    
    # ===== FINAL RESULTS =====
    steps.append("")
    steps.append("# 📊 **SEARCH COMPLETED**")
    steps.append("---")
    
    # Final visualization
    if found:
        final_vis = create_visualization(arr, -1, -1, -1, position)
        visual_steps.append(final_vis)
        
        steps.append(f"## ✅ **SUCCESS**")
        steps.append(f"**Target Found:** {target}")
        steps.append(f"**Position:** Index {position} in sorted array")
        steps.append(f"**Original Array Index:** {original_arr.index(target)}")
        result_msg = f"🎯 Target {target} found!"
    else:
        final_vis = "```\n❌ TARGET NOT FOUND\nTarget value is not present in the array.\n```"
        visual_steps.append(final_vis)
        
        steps.append(f"## ❌ **NOT FOUND**")
        steps.append(f"Target {target} is not in the array.")
        result_msg = f"❌ Target {target} not found."
    
    # Statistics
    steps.append("")
    steps.append("## 📈 **ALGORITHM STATISTICS**")
    steps.append(f"- **Total Steps:** {step_count}")
    steps.append(f"- **Comparisons Made:** {comparisons}")
    steps.append(f"- **Array Size:** {len(arr)} elements")
    steps.append(f"- **Time Complexity:** O(log n) = O(log {len(arr)})")
    steps.append(f"- **Space Complexity:** O(1) - constant extra space")
    
    # Prepare return values
    steps_text = "\n".join(steps)
    current_vis = visual_steps[-2] if len(visual_steps) > 1 else visual_steps[0]
    final_vis = visual_steps[-1]
    
    # Create stats box
    stats = f"""
    **Algorithm:** Binary Search
    **Status:** {'Found ✓' if found else 'Not Found ✗'}
    **Target:** {target}
    **Array Size:** {len(arr)}
    **Steps:** {step_count}
    **Comparisons:** {comparisons}
    **Time Complexity:** O(log n)
    """
    
    return steps_text, current_vis, final_vis, stats

# ===== GRADIO INTERFACE =====
with gr.Blocks(title="CISC 121 - Binary Search Visualizer") as demo:
    
    # Header
    gr.Markdown("""
    # 🔍 CISC 121 Project: Binary Search Algorithm Visualizer
    ### **Visual Simulation of Binary Search Algorithm**
    *Interactive step-by-step demonstration for educational purposes*
    """)
    
    # Main content in rows
    with gr.Row():
        # Left column: Input controls
        with gr.Column(scale=1):
            gr.Markdown("### 📝 **Input Parameters**")
            
            arr_input = gr.Textbox(
                label="Enter Numbers (comma-separated)",
                placeholder="Example: 23, 5, 17, 42, 9, 31, 14, 8",
                value="23, 5, 17, 42, 9, 31, 14, 8",
                info="Enter numbers separated by commas"
            )
            
            target_input = gr.Textbox(
                label="Target Number to Find",
                placeholder="Enter the number to search for",
                value="17",
                info="The number you want to find in the array"
            )
            
            with gr.Row():
                run_btn = gr.Button("🚀 Run Binary Search", variant="primary", scale=2)
                clear_btn = gr.Button("🗑️ Clear All", variant="secondary", scale=1)
            
            # Predefined examples
            gr.Markdown("### 🧪 **Quick Examples**")
            with gr.Row():
                gr.Button("Example 1: 1-9, Find 5", size="sm").click(
                    lambda: ("1,2,3,4,5,6,7,8,9", "5"),
                    outputs=[arr_input, target_input]
                )
                gr.Button("Example 2: Even numbers, Find 12", size="sm").click(
                    lambda: ("2,4,6,8,10,12,14,16,18,20", "12"),
                    outputs=[arr_input, target_input]
                )
                gr.Button("Example 3: Random, Find 99", size="sm").click(
                    lambda: ("15,25,35,45,55,65,75,85,95", "99"),
                    outputs=[arr_input, target_input]
                )
    
    # Middle row: Output displays
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### 📖 **Algorithm Steps**")
            steps_output = gr.Markdown(
                label="Step-by-Step Process",
                value="Enter numbers and click 'Run Binary Search' to begin..."
            )
        
        with gr.Column(scale=1):
            gr.Markdown("### 📊 **Statistics**")
            stats_output = gr.Markdown(
                label="Algorithm Statistics",
                value="Statistics will appear here after running the search."
            )
    
    # Bottom row: Visualizations
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 👁️ **Current Step Visualization**")
            current_vis_output = gr.Code(
                label="Array Visualization",
                language="markdown",
                lines=12,
                value="Visualization will appear here..."
            )
        
        with gr.Column():
            gr.Markdown("### 🏁 **Final Result**")
            final_vis_output = gr.Code(
                label="Final State",
                language="markdown",
                lines=12,
                value="Final result will appear here..."
            )
    
    # Educational information (collapsible)
    with gr.Accordion("📚 **Learn About Binary Search**", open=False):
        gr.Markdown("""
        ## **How Binary Search Works**
        
        **Algorithm Steps:**
        1. **Requirement:** Input array must be sorted in ascending order
        2. **Initialize:** Set low = 0, high = length - 1
        3. **Find Middle:** mid = (low + high) // 2
        4. **Compare:**
           - If arr[mid] == target: **Found!** Return mid
           - If arr[mid] < target: Search RIGHT half (low = mid + 1)
           - If arr[mid] > target: Search LEFT half (high = mid - 1)
        5. **Repeat** steps 3-4 until found or low > high
        
        ## **Key Characteristics**
        - **Time Complexity:** O(log n) - Very efficient for large arrays
        - **Space Complexity:** O(1) - Uses constant extra space
        - **Requirements:** Array must be sorted, random access needed
        
        ## **Why Choose Binary Search?**
        - Extremely efficient for searching in large datasets
        - Demonstrates divide-and-conquer strategy
        - Clear visual representation possible
        - Fundamental algorithm in computer science
        """)
    
    # Testing examples section
    gr.Markdown("### 🧪 **Testing Examples**")
    examples = gr.Examples(
        examples=[
            ["1,2,3,4,5,6,7,8,9,10", "7"],
            ["10,20,30,40,50,60,70", "25"],
            ["100,200,300,400,500", "300"],
            ["5,15,25,35,45,55,65", "10"],
            ["2,4,8,16,32,64,128", "32"]
        ],
        inputs=[arr_input, target_input],
        outputs=[steps_output, current_vis_output, final_vis_output, stats_output],
        fn=binary_search_visual,
        cache_examples=False,
        label="Click any example to test:"
    )
    
    # Button actions
    run_btn.click(
        fn=binary_search_visual,
        inputs=[arr_input, target_input],
        outputs=[steps_output, current_vis_output, final_vis_output, stats_output]
    )
    
    def clear_all():
        return "", "", "", "", "", ""
    
    clear_btn.click(
        fn=clear_all,
        outputs=[arr_input, target_input, steps_output, current_vis_output, final_vis_output, stats_output]
    )

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    demo.launch()