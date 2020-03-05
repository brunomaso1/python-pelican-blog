# BLOG

This blog contents post about serveral topics in IT, focusing on artificial intelligence, quantum computer and robotics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- [Python](https://maven.apache.org/)
- [Pelican](https://maven.apache.org/)
- [Git](https://maven.apache.org/)
- [Anaconda](https://maven.apache.org/)

### Pelican

**Pelican theme:**
- [Alchemy](https://github.com/nairobilug/pelican-alchemy) 

**Pelican plugins:**
- [ipynb](https://github.com/danielfrg/pelican-ipynb)
- [bootstrapify](https://github.com/ingwinlu/pelican-bootstrapify)

## Deployment

To deploy this blog localy, you should follow next steps (after install all the prerequisites):

### Built With

- [pip](https://maven.apache.org/) - Build system 

### Process

1. Create new enviroment on Anaconda:
	1.1 Open Anaconda Navigator and select "Environments".
	1.2 Create a new enviroment.
	1.3 After created select the "play" button and select "Open Terminal".

2. Clone this repo wherever you want:
```
git clone https://github.com/brunomaso1/blog.git
```

3. Add a new post (can be jupyter notebook or md), on "post" folder inside "Content".

4. Build the blog with pelican:
```
pelican content
```

5. Test the blog:
	5.1 Initiate pelican server on the output folder:
	```
	python -m pelican.server
	```
	5.2 Open the blog on the browser on "localhost:8000"

6. Modify publishconf.py to set your URL to the post.

7. Build the blog with the new configuration:
```
pelican content -s publishconf.py
```

8. Publish the blog via ghp-import
```
ghp-import output
git push origin gh-pages
```

9. Test and commit changes!
