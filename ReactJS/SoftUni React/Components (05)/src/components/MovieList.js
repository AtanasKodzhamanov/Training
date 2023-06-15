// import { createElement } from 'react';
import Movie from "./Movie";

export default function MovieList({
    movies,
    onMovieDelete,
    onMovieSelect,
}) {
    // let movieElements = [];
    // for (const movie of movies) {
    //     // movieElements.push(createElement(Movie, movie));
    //     movieElements.push(<li><Movie {...movie} /></li>);
    // }

    // let movieList = movies.map(movie => <li><Movie {...movie} /></li>);

    // Take the movies object map it and pass each movie object to the Movie component as props. The Movie component will then render the movie object.
    return (
        <ul>
            {movies.map((movie) => (
                <li key={movie.id} >
                    <Movie
                        {...movie}
                        onMovieDelete={onMovieDelete}
                        onMovieSelect={onMovieSelect}
                    />
                </li>
            ))}
        </ul>
    );
};