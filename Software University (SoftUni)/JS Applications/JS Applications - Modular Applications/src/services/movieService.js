// deals with taking movies from the database and returning them to the client

const baseUrl = 'http://localhost:3030/data/movies';

export const  getAll =() =>
    fetch(`${baseUrl}`)
    .then(res => res.json());