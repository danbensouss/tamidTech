# McViewer Documentation

## Wiki Link

* For further explanation of the features of this project, check out the [project wiki](https://github.com/danbensouss/TAMID-Youtube-Viewer/wiki). 

## Development Process

My development process began figuring out how to configure Heroku with my project. After that was completed I went on to brainstorm quickly about what models I would need to write for the site. Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database. Once I had written out the models.py file, I went on the implement the different pages I would need.  
One by one, I would write a URL path in the urls.py file and then I would write the view method in views.py which would render each of the specified paths. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data. A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates. In those methods, the entire backend logic of the system is implemented.

## Challenges Faced

The main challenged I faced throughout the development of McViewer actually occured at the very beggining. As many developpers know, it is often the configuration of settings files and databases that prove most challenging in web development projects. I had never used Heroku before but decided it was time to learn! I had to get some help from a friend of mine who helped configure Heroku properly with my Django app. Im thankful to have encountered this challenge because I definitely came out of it with more knowledge on how to deploy my future projects to the cloud. 

## Additional Features

For this project I really wanted to try to show off my skills at building a system that allows users to interact with one another. I developed McViewer as a sort of network for like-minded individuals to share the video content they are watching ond searching through. Anyone with a McViewer account has access to the Network page where they can see what other people who also have access to this private Youtube search engine are searching for. Furthermore, the ability to create and join a private network allows users to join an exclusive group of people that can only see each others searches! I think of it as a sort of instagram but for Youtube searches! If I had more time, I would have loved to expand on this concept and really see how a simple concept like this can translate into a sort of social network for video content that similar people are browsing through. Something that could be added quite simply is a filter which takes in a list of the specific categories of each video present on one of the given network page. With that list the filter would then determine if any of the video categories are the same, and if they are, I can display a list of recommended videos from that category on their network page! This would be cool since it would already be clear that individuals in that given network are already interested in that category of video content.  
