# GenAI-Powered Linux Command Automation

## Overview  
This project integrates Generative AI with Linux operations (GenAI + Ops). It allows users to enter natural language instructions, which are then converted into executable Linux commands. The script executes these commands and returns the results, making Linux operations more efficient and user-friendly.

## Features  
- Converts natural language into shell commands.  
- Executes system-level operations such as file management, process monitoring, and configuration.  
- Reduces repetitive manual typing and minimizes errors.  
- Demonstrates the practical use of AI in DevOps environments.  

## Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Omprakashkumar01/automation_of_command_linux.git
   cd automation_of_command_linux
   ```
2. Run the script:  
   ```bash
   python automate_linux_command.py
   ```
3. Example input/output:  
   ```
   Input: "Show me disk usage in the home directory"
   Generated Command: du -h ~
   Output: [command result]
   ```

## Tech Stack  
- Python  
- Linux Shell  
- Generative AI (API integration if applicable)  

## Future Scope  
- Add a dry-run mode to validate commands before execution.  
- Implement logging and auditing for executed commands.  
- Extend support for multi-step workflows (e.g., backup, compress, and upload logs).  
- Integrate with chat platforms or CI/CD pipelines for real-time operations.  
