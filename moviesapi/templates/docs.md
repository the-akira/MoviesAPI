
<a id="intro"></a>
# Introduction

Welcome to the <span>Movies API Documentation</span> here you will better understand the details about the available resources and also learn how to consume them through [HTTP requests](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html).

- - -

<a id="start"></a>
## Getting Started

Movies API is an API focused on reading resources, for this reason we will use the [GET method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) with it in most scenarios to obtain our resources in JSON format and use it in the way that is most convenient for us.

There are several ways to execute HTTP requests, either through a web browser, a programming language like [Python](https://requests.readthedocs.io/en/master/) or [Javascript](https://github.com/axios/axios), or with software like [curl](https://github.com/curl/curl) or [httpie](https://httpie.org/). For this specific task we will use httpie for its simplicity. So let's start by asking for resources about the game genres. Open up your terminal and type

```
http https://moviesapi.herokuapp.com/api/genres/
```

We will immediately receive the following resource in response

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 307
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 13:05:25 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 13,
	    "next": "http://127.0.0.1:8000/api/genres/?page=2",
	    "previous": null,
	    "results": [
	        {
	            "id": 1,
	            "name": "Horror"
	        },
	        {
	            "id": 2,
	            "name": "Adventure"
	        },
	        {
	            "id": 3,
	            "name": "Science Fiction"
	        },
	        {
	            "id": 4,
	            "name": "Action"
	        },
	        {
	            "id": 5,
	            "name": "Drama"
	        },
	        {
	            "id": 6,
	            "name": "Fantasy"
	        },
	        {
	            "id": 7,
	            "name": "Historical"
	        },
	        {
	            "id": 8,
	            "name": "Mystery"
	        }
	    ]
	}

As we can see, several game genres are returned to us with their respective ids and names

- - -

<a id="base"></a>
## Base URL

The base URL is the root URL of the API's and it can serve as a map to locate us and understand the resources that are at our disposal. The base URL for the Video Games API is as follows

```
https://moviesapi.herokuapp.com/api/
```

Consider this root URL as the basis for our future requests

- - -

<a id="auth"></a>
## Authentication

<span>Movies API</span> is a completely open API, without the need for authentication or token generation to obtain the data

- - -

<a id="search"></a>
## Search Filter

The SearchFilter class supports simple single query parameter based searching, and is based on the Django admin's search functionality. Each resource has a field in which we can query specific data. Let's look at an example to illustrate the idea!

Let's make an HTTP request to the following URL

```
http http://moviesapi.herokuapp.com/api/movies/?search=Space
```

We will get a filtered response only from the movies we want

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 2140
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 13:16:31 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 1,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	            "cast": [
	                "Keir Atwood Dullea",
	                "Gary Lockwood"
	            ],
	            "country": "United States of America",
	            "cover": "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/2001_A_Space_Odyssey_%281968%29.png/220px-2001_A_Space_Odyssey_%281968%29.png",
	            "created": "2020-09-22T20:54:48.360601Z",
	            "director": "Stanley Kubrick",
	            "edited": "2020-09-22T20:54:48.360717Z",
	            "genre": [
	                "Science Fiction"
	            ],
	            "id": 2,
	            "language": "English",
	            "magnet": "magnet:?xt=urn:btih:809B856531647878BEF0044AD04A785CBBEDF708&dn=2001.A.Space.Odyssey.1968.1080p.BluRay.x264.anoXmous&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce",
	            "release_date": "1968-04-02",
	            "running_time": "142 minutes",
	            "screenshots": [
	                {
	                    "url": "https://ychef.files.bbci.co.uk/976x549/p0639ffn.jpg"
	                },
	                {
	                    "url": "https://a.ltrbxd.com/resized/sm/upload/x3/fx/ae/ju/2001-space-odyssey-120-1200-1200-675-675-crop-000000.jpg"
	                },
	                {
	                    "url": "https://mcmscache.epapr.in/post_images/website_350/post_15668452/thumb.jpg"
	                }
	            ],
	            "synopsis": "2001: A Space Odyssey is a 1968 British-American epic science fiction film produced and directed by Stanley Kubrick. The screenplay was written by Kubrick and Arthur C. Clarke, and was inspired by Clarke's 1951 short story \"The Sentinel\" and other short stories by Clarke. A novel released after the film's premiere was in part written concurrently with the screenplay. The film, which follows a voyage to Jupiter with the sentient computer HAL after the discovery of an alien monolith affecting human evolution, deals with themes of existentialism, human evolution, technology, artificial intelligence, and the possibility of extraterrestrial life.",
	            "title": "2001: A Space Odyssey",
	            "trailer": "https://www.youtube.com/watch?v=oR_e9y-bka0",
	            "url": "http://127.0.0.1:8000/api/movies/2/"
	        }
	    ]
	}

In this case the movie was filtered by title

- - -

<a id="pagination"></a>
## Pagination

Movies API provides data through chunks that can be paged. Let's request the second page of movies genres to get an idea of how this mechanism works

Let's request the following URL

```
http https://moviesapi.herokuapp.com/api/genres/?page=2
```

Immediately we obtain the respective data on the second page of Movies genres

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 218
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 13:19:00 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 13,
	    "next": null,
	    "previous": "http://127.0.0.1:8000/api/genres/",
	    "results": [
	        {
	            "id": 9,
	            "name": "Romance"
	        },
	        {
	            "id": 10,
	            "name": "Thriller"
	        },
	        {
	            "id": 11,
	            "name": "Musical"
	        },
	        {
	            "id": 12,
	            "name": "Documentary"
	        },
	        {
	            "id": 13,
	            "name": "War"
	        }
	    ]
	}

Through pagination we can browse all available data.

- - -

<a id="encoding"></a>
## Encoding

JSON is the standard data format provided by Video Games API by default. You can see details about Schema at the following URL: [API Schema](https://moviesapi.herokuapp.com/api/schema/)

- - -

<a id="root"></a>
## Root

The Root resource provides information on all available resources within the API.

Example request:

```
http https://moviesapi.herokuapp.com/api/
```

We will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 187
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 14:18:50 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "actors": "http://127.0.0.1:8000/api/actors/",
	    "directors": "http://127.0.0.1:8000/api/directors/",
	    "genres": "http://127.0.0.1:8000/api/genres/",
	    "movies": "http://127.0.0.1:8000/api/movies/"
	}

### Root Attributes

- <span>Actors</span>: String, The URL root for Actors resources
- <span>Directors</span>: String, The URL root for Directors resources
- <span>Genres</span>: String, The URL root for Genre resources
- <span>Movies</span>: String, The URL root for Movies resources

- - -

<a id="movies"></a>
## Movies

A movie resource represents a movie object with several attributes

### Endpoints

- <span>/api/movies/</span>: Get all the movies resources
- <span>/api/movies/{id}</span>: Get a specific movie

Example request:

```
http https://moviesapi.herokuapp.com/api/movies/1/
```

We will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 2203
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 14:23:12 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "cast": [
	        "Elijah Wood",
	        "Ian Murray McKellen"
	    ],
	    "country": "New Zealand",
	    "cover": "https://upload.wikimedia.org/wikipedia/en/8/8a/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29.jpg",
	    "created": "2020-09-22T20:53:14.315935Z",
	    "director": "Peter Jackson",
	    "edited": "2020-09-22T20:53:14.316131Z",
	    "genre": [
	        "Adventure",
	        "Fantasy"
	    ],
	    "id": 1,
	    "language": "English",
	    "magnet": "magnet:?xt=urn:btih:E175ACD03B68BF0736DFC4B17D1D1496A455E01D&dn=The%20Lord%20of%20the%20Rings%3A%20The%20Fellowship%20of%20the%20Ring%20EXTENDED%20(2001&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce",
	    "release_date": "2001-12-10",
	    "running_time": "178 minutes",
	    "screenshots": [
	        {
	            "url": "https://cdn.britannica.com/35/201735-050-0B3066E6/Scene-The-Lord-of-the-Rings-Fellowship.jpg"
	        },
	        {
	            "url": "https://3m7ajlsrzj92lfd1hu16hu7vc-wpengine.netdna-ssl.com/wp-content/uploads/2019/07/LordOTRingsFellowship-660x350-1562562055.jpg"
	        }
	    ],
	    "synopsis": "The Lord of the Rings: The Fellowship of the Ring is a 2001 epic fantasy adventure film directed by Peter Jackson, based on the 1954 novel The Fellowship of the Ring, the first volume of J. R. R. Tolkien's The Lord of the Rings. The film is the first instalment in The Lord of the Rings trilogy. It was produced by Barrie M. Osborne, Jackson, Fran Walsh and Tim Sanders, and written by Walsh, Philippa Boyens and Jackson. The film features an ensemble cast including Elijah Wood, Ian McKellen, Liv Tyler, Viggo Mortensen, Sean Astin, Cate Blanchett, John Rhys-Davies, Billy Boyd, Dominic Monaghan, Orlando Bloom, Christopher Lee, Hugo Weaving, Sean Bean, Ian Holm, and Andy Serkis. It is followed by The Two Towers (2002) and The Return of the King (2003).",
	    "title": "The Lord of the Rings: The Fellowship of the Ring",
	    "trailer": "https://www.youtube.com/watch?v=V75dMMIW2B4",
	    "url": "http://127.0.0.1:8000/api/movies/1/"
	}

### Movies Attributes

- <span>id</span>: Integer, Unique id representing a movie
- <span>title</span>: String, Represents the title of the respective movie
- <span>synopsis</span>: String, Represents the synopsis of the respective game
- <span>cover</span>: String, image URL representing the movie cover
- <span>trailer</span>: String, video URL representing the movie trailer
- <span>screenshots</span>: Object, images URL representing scenes of the movie
- <span>director</span>: String, representing the director of the movie
- <span>cast</span>: Array, An array of actors name representing the actors of the movie
- <span>genre</span>: Array, An array of genres name representing the genres of the movie
- <span>release_date</span>: String, Represents the date on which the movie was released
- <span>running_time</span>: String, Represents the total running time of the movie (in minutes)
- <span>country</span>: String, Represents the country in which the movie was produced
- <span>language</span>: String, Represents the main language spoken in the movie
- <span>magnet</span>: String, Represents the link magnet to download the movie
- <span>created</span>: String, Represents the date in which this resource was created
- <span>edited</span>: Represents the date in which this resource was edited
- <span>url</span>: Represents the URL of this resource

- - -

<a id="genres"></a>
## Genres

A genre resource represents a movie genre

### Endpoints

- <span>/api/genres/</span>: Get all the genres resources
- <span>/api/genres/{id}</span>: Get a specific genre

Example request:

```
http https://moviesapi.herokuapp.com/api/genres/
```

We are going to receive the following response from the server:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 307
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 14:39:28 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 13,
	    "next": "http://127.0.0.1:8000/api/genres/?page=2",
	    "previous": null,
	    "results": [
	        {
	            "id": 1,
	            "name": "Horror"
	        },
	        {
	            "id": 2,
	            "name": "Adventure"
	        },
	        {
	            "id": 3,
	            "name": "Science Fiction"
	        },
	        {
	            "id": 4,
	            "name": "Action"
	        },
	        {
	            "id": 5,
	            "name": "Drama"
	        },
	        {
	            "id": 6,
	            "name": "Fantasy"
	        },
	        {
	            "id": 7,
	            "name": "Historical"
	        },
	        {
	            "id": 8,
	            "name": "Mystery"
	        }
	    ]
	}

### Genre Attributes

- <span>id</span>: Integer, Unique id representing a genre
- <span>name</span>: String, Represents the name of the respective genre

- - -

<a id="directors"></a>
## Directors

A director resource represents a movie director

### Endpoints

- <span>/api/directors/</span>: Get all the directors resources
- <span>/api/directors/{id}</span>: Get a specific director

Example request:

```
http https://movies.herokuapp.com/api/directors/?search=Stanley
```

Realize that we have searched for a director by his name through the search filter funcionality and we will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 269
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 14:45:48 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "count": 1,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	            "country": "United States of America",
	            "id": 1,
	            "movies": [
	                {
	                    "id": 2,
	                    "title": "2001: A Space Odyssey"
	                }
	            ],
	            "name": "Stanley Kubrick",
	            "photo": "https://upload.wikimedia.org/wikipedia/commons/d/da/KubrickForLook_%28cropped%29.jpg"
	        }
	    ]
	}

### Director Attributes

- <span>id</span>: Integer, Unique id representing a director
- <span>name</span>: String, Represents the name of the director
- <span>photo</span>: String, URL of a director's photo
- <span>country</span>: String, Represents the country the director was born in
- <span>movies</span>: Object, Represents the movies directed by him

- - -

<a id="actors"></a>
## Actors

A actor resource represents a movie actor

### Endpoints

- <span>/api/actors/</span>: Get all the actors resources
- <span>/api/actors/{id}</span>: Get a specific actor

Example request:

```
http https://movies.herokuapp.com/api/actors/1/
```

We are requesting the actor which has the id 1. We will get the following response:

	HTTP/1.1 200 OK
	Allow: GET, HEAD, OPTIONS
	Content-Length: 234
	Content-Type: application/json
	Date: Fri, 25 Sep 2020 14:54:29 GMT
	Referrer-Policy: same-origin
	Server: WSGIServer/0.2 CPython/3.7.7
	Vary: Accept, Cookie
	X-Content-Type-Options: nosniff
	X-Frame-Options: DENY

	{
	    "country": "United States of America",
	    "id": 1,
	    "movies": [
	        {
	            "id": 2,
	            "title": "2001: A Space Odyssey"
	        }
	    ],
	    "name": "Keir Atwood Dullea",
	    "photo": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Keir_Dullea_Denver_Pyle_1962_%28cropped%29.JPG"
	}

### Actor Attributes

- <span>id</span>: Integer, Unique id representing a actor
- <span>name</span>: String, Represents the name of the actor
- <span>photo</span>: String, URL of a actor's photo
- <span>country</span>: String, Represents the country the actor was born in
- <span>movies</span>: Object, Represents the movies acted upon by him

- - -

<a id="schema"></a>
## Schema

API schemas are a useful tool that allow for a range of use cases, including generating reference documentation, or driving dynamic client libraries that can interact with your API.

You can find Schema for the Movies API by visiting the following link: [Schema API](https://moviesapi.herokuapp.com/schema)

- - -

<a id="contribution"></a>
## Contribution

You can contribute to the Movies API project in several ways

- Fork or Star the project on [Github](https://github.com/the-akira/MoviesAPI)
- Share it with your friends in Social Medias
- Help to improve the Code, Data Models and Documentation

- - -

<a id="playground"></a>
## Playground

Django Rest framework provides us with an interface that we can [try the API](https://moviesapi.herokuapp.com/api) without the need for any tool.