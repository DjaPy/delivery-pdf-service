 # PDF delivery

The service consists of two microservices.
 - handler html code and the initiator of the call processing html is written
  in aiohttp
 - simple, Docker-powered PDF conversions athena - read more [here](https://github.com/arachnys/athenapdf)
 
 Which communicate with each other via http.

# Build and run

- Clone the repository to your computer.
- Configure `example.env` and rename to `.env`.
- From the root directory of the project, run the `docker build --tag=testconvertpdf .`
- Start docker-compose `docker-compose up`
- The service is ready to use.

#How to use

Any client make a post request to the address `0.0.0.0:8500` and pass any html.
In response, you will receive a generated pdf.

