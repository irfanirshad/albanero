# Download node 
FROM node:12



# Every instruction in this dockerfile is considered its own step or layer
WORKDIR /app




# we dont want to have to reinstall our node modules
# every time we change our source code
COPY package*.json ./

# after this we can run npm install
RUN npm install


# THis COPY will be used to copy our source over and will be our Layer 4
# But wait, don't we already(assume we do) have a local package.json file. We dont want to have extra problems with clashing
# so we introduce a .dockerignore file just like .gitignore 
# After that we can safely add the COPY command to copy our source code
COPY . .

# ENv variable
ENV PORT=8080 


# listen on this port at runtime
# NOTE: localhost:8080 wont work unless you specify a map from docker's port to our localmachine's port
# use the following command to do so:
# docker run -p <LOCAL_PORT>:<CONTAINER_PORT> <container-image>
# docker run -p 5000:8000 <container-image> 
EXPOSE 8080


# ONLY ONE OF THESE PER DOCKERFILE
# an array of strings
# doesnt spin up a shell session here 
CMD ["npm", "start"]