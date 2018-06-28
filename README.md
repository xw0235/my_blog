## This is the project to build my personal blog        
Today I create a new project to build my personal blog.I'll record the whole process of building my personal blog in this markdown file.
```bash
# to active the virtualenv
source env/bin/active
# cerate a Django project
django-admin startproject my_blog
# cd to the dir of 'my_blog'
cd my_blog
# cerate a app
./manage startapp blogApp
```
Now,I'll analyze the overall structure of my blog. 

- That front paage

    - The index

        - A navigation bar

        - Use the pictures to take turns to play

        - The container of the articles

    - Each articles' page

        - Of cause it also need a navigationg bar

        - Messages?No,we don't have other users

        - We should allow readers to share my article

- That back-end

    - To post the articles 

        - I'm going to use that UE

        - It must to support grammar of Markdown

    - The Articles list

        - I can manage the articles in the list

        - I can get the views of all the articles

That's all I can think about right now.    OK,now I'll open my VSCode to edit my code.      