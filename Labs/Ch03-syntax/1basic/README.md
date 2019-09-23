# Chapter 3: Lab 1 Create a basic program

## Objectives
* Execute code multiple ways
* Receive input from user
* Receive input from terminal

## Part 1 Run files two ways

1. Create a new folder in your MyPython project folder called Ch03. You can do this by right-clicking on the folder and choosing new folder.

 ![new folder icon](../screenshots/1-new-folder.png)

2. Create a new file in this folder called basic.py by right-clicking on the folder and choosing new file.

    ![](../screenshots/2-new-file.png)

1. In the file, add a print() statement with the message
   Hello and Welcome to a basic python program

    ![](../screenshots/3-unsaved.png
)
1. Your code will now have changes and will not be saved. This is indicated by both the vertical menu and the tab at the top of the editor.  Always save your changes! If you ever get rid of code you need etc, you can use GIT to recover it. Oftentimes if you do not see anything new it is due to an unsaved file.

1. The fastest way to manually save your file is by using Control + S. Save your file now. There will not be more directions to save before running your files, be sure to do this each time.
   
   An alternative is to choose to automatically save your files in VSCode.

   ![](../screenshots/4-autosave.png)


1. Execute your file by right clicking in the editor and choosing Run Python In Terminal
    ![](../screenshots/run-python-from-menu.png)

1. Now ask the user to enter their favorite food by using input(). Assign the response to a variable called food. And display a message using the variable.

    ![input](../screenshots/5-input.png) 

    Note the use of a space before the closing quote. This makes entering input easier to read.

1. Try to run by right click menu as before, and you will get an error. Asking for input doesn't work well from this menu. If this does work for you, tell your instructor that it has been fixed in the extension!

2. We must run from the terminal in the correct location. Use the Explorer pane of VS Code. Right click on the file and choose Open in Terminal.

    ![input](../screenshots/7-right-click-terminal.png)

3. From the prompt, now you can start the script with the Python interpreter using **py basic.py**

4. Your code should now receive input and use it to display back to the user.
    
    You can keep executing by returning to the terminal and hitting the up arrow to repeat the last command.

   

## Part 2 use a standard library

1. Let's change our welcome message. First comment out the current print statement by putting your cursor on the print line and hit **control + /**

    ![comment](../screenshots/6-comment.png) 

    This VS Code shortcut applies the appropriate comment type regardless of the coding language.

2. Import the package called **sys** at the top of your file. Module imports by convention should go at the top so that they are easy to locate. Then use **sys.argv** to get a passed in argument.

    ```python
        import sys

        print('Hello, ' + sys.argv[1] + ' and Welcome to a basic python program')
    ```

3.  Make sure you are running the program from the terminal, and this time pass in an argument

    ![comment](../screenshots/8-pass-arg.png)

4.  Try to run without argument and see error. we will be handling errors in the future, for now, we nee to be careful about how we use our programs.

    ![comment](../screenshots/9-error.png)



5.  Mark your work as complete using the appropriate method.


