# Chapter 2: Lab 1: Practice with Python in VS Code IDE 

## Objectives
* Open README.md in VS Code in Preview Mode
* Install VS Code extensions for Python
* Practice using VS Code to execute Python code

## Table of Contents

[Part 1 - Use Preview Mode](#part-1---markdown-md-files-in-edit--preview-mode)

[Part 2 - Discard tracked changes](#part-2---git-is-tracking-your-changes)

[Part 3 - Install VS Code extensions](#part-3-install-vs-code-extensions)

[Part 4 - Run Python Code](#part-4---run-python-code)


### **Part 1 - Markdown .md files in Edit & Preview Mode**

    We use markdown files in this class as they are used extensively in the industry with modern  projects.  They are plain text files that end in the extension `.md` and use special characters to indicate the meaning of text and how to display it when used on websites.
    
    The The Python Package Index (PyPI) is a repository of software for the Python programming language. It uses the README.md to display info for each package.
    
    On sites such as GitHub and Bitbucket, the README is automatically displayed from the root of the repository. 
    
    If you like to use Reddit you can use markdown to style your posts.
    
    The default mode of VS Code opens `.md` files in EDIT MODE where you see the special characters for formatting. VS Code also offers a PREVIEW MODE so you can more easily read the styled text.

    We will look at multiple ways to open markdown files in PREVIEW MODE in VS Code. You will use these methods for lab exercises and some demos. 
    
**Shortcut CTRL-SHIFT-V**

1. If you are viewing this on GitHub, make sure you open this same README.md file within VS Code. Make sure the file is in focus - (click this text in the VS Code editor if the document has lost focus). 
   
2. Now you can open a new tab in PREVIEW MODE by hitting control-shift-V. This will open the preview in a new tab. You can then switch back and forth using the tabs.
   
    **OPENING A SPLIT SCREEN**

3. Open a Split screen in order to view both at the same time by clicking on this icon 
![Open Split Screen](../screenshots/open-split-screen.png)

1. Drag the tab to the other window.
![Open In Preview](../screenshots/dragtabs.png)

        You should now see the two files at the same time. With both Edit mode and Preview mode open in split panes, notice that if you scroll in one, the other scrolls as well.

        Remember this process to split the panes, it is helpful when you want to see multiple files at the same time.

    **VERTICAL MENU BUTTONS TOGGLE**

1. Give yourself more room to view code by hiding the leftmost pane. It should currently be the Explorer pane. Clicking the Explorer pane icon - pictured here with a blue circle and 1 will toggle this view. All of the icons in this vertical menu can be toggled to give you more room to work. Practice clicking to show and hide the various menus.

    ![Vertical Pane](../screenshots/vertical-pane.png)

**MARKDOWN FORMATTING**

3. Make sure you can see both the Edit Mode in VS Code and the Preview Mode in VS Code (or GitHub view).
   
    Note the following:

    * Hash marks (#), are used for formatting headings.
        * A single # is heading "level 1" which is biggest, ## is "level 2", slightly smaller, and so on.
    * The asterisk is used to make a bullet.
        * Tabs are used for indentation of bullets.
    * Text can be highlighted using `backticks` around key words.
    * Code can be made **bold** using double asterisks.
    * Every item can be numbered as 1 in Edit Mode. When the markdown file is rendered: in preview mode or in browsers - the numbers will increment correctly.
        * This makes it easy to insert new items or re-order items, without needing to take the time to renumber.


    **OPEN PREVIEW TO SIDE**

4. Close all tabs so only the README.md is open in Edit Mode.
   
5. When a markdown file is the active file, there is a button that automatically opens Preview in the split pane.
![Preview button](../screenshots/preview-button.png)

        Most everything in VS Code has a hover effect. If you forget what anything does, just hover over it.

    **OPENING FROM EXPLORER**
1. In VS Code, from the Explorer Pane, you can find the markdown file of interest, right click and choose **Open Preview**. Try this now with this README.md as shown.
![Open In Preview](../screenshots/1-open-preview.png)

1. In VS Code, while viewing in Preview mode, if you double-click an area of the file, you will be taken back to the EDIT VIEW or "source" markdown file for editing.

    Notice that if you double click the  image shown above - it takes you to the edit mode version where the image is linked.

2.  For the rest of this lab exercise, view this file in Preview mode. Either on GitHub or in a tab of VS Code.

### **Part 2 - Git is tracking your changes**

1. In 200Python it is safe to modify files, because the Demos and Labs folders are tracked by Git.

2. Making changes to the repository.
    
    a. While viewing this README.md file in Edit Mode, in the space provided below, type in your name.

    **Name: Put Your name here**
    
    b. Save this file by clicking the drop-down menu File | Save or by hitting CTRL-S to save. (get used to Ctrl-S if you are not already - it will save you a lot of time.)

    c. Now that your change has been saved, look at the Source Control icon in the  left-side navigation bar. You should see a number now. 
    

    ![Source control](../screenshots/source-control.png)

    d. Click on this icon.  This opens the Source Control pane with a list of files that have been changed. If you haven't modified anything else, you should only see one file, this README.md. 

    e. You can compare changes by clicking on the name of the file. This brings up a nice graphical diff tool of the changes. 

    ![Diff](../screenshots/diff.png)


    f. Discard the changes made in a single file by hovering over the file name to reveal a menu, and clicking the left facing circular arrow with the title of "Discard Changes". Do this now to discard changes you made to README.md. The number should then disappear.  

    ![discard-changes-file.png](../screenshots/discard-changes-file.png)

    * If you end up with many changes, you can discard all changes by hovering over the word CHANGES to reveal a menu on that level, and clicking on the **discard all changes** icon.

![Discard Changes](../screenshots/discard-changes.png)


### **Part 3: Install VS Code extensions**

    The extensions pane allows you to search for, install, disable and remove extensions easily.

1. Look on the left side bar menu of VS Code and click on the `Extensions` icon or use the shortcut (Ctrl + Shift + X). 

    ![extensions](../screenshots/extensions.png)


2. Type into the Extensions Marketplace search field to find `Python` by Microsoft. If you do not have it already installed click the install button.

    
    ![extensions](../screenshots/1-search-python-extension.png
)

    Sometimes that is all you do - install. For some extensions there are additional options.


1. Follow a similar workflow as above to download these VS Code Extensions. Read their pages to see what they do. 

* GitLens -Eric Amodio
* Bracket Pair Colorizer 2 - CoenraadS


### **Part 4 - Run Python Code** 

#### Execute Code
1. In the Explorer pane, expand to the directory \Demos\Ch02-execute-python\
 ![](../screenshots/1open-terminal.png)

1. Open integrated terminal in VS code, right click the Ch02 directory and choose Open in Terminal 
 
1. From prompt start typing py the name of the file, and hit tab after the first 4 letters. 

    ![](../screenshots/2-tab-complete-run.png)

1. After it autocompletes, hit enter to run the program.
   
2. Highlight the print line with Goodbye, and right-click. Choose Run Selection. You should only see this line execute. Repeat running this line by using Shift + Enter
 ![](../screenshots/3-run-selection.png)

1. Mark your work as complete before moving on to the bonus.  

## Bonus

1. Open the directory z_cheatsheets and look over the VS Code markdown.
   
2. Open the Interactive Playground from the VS Code Help menu and explore what is possible.
