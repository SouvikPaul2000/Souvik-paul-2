FROM node
RUN apt update -y
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .

CMD ["npm" , "start"]
