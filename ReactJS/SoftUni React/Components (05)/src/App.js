import { useState, useEffect } from 'react';

import MovieList from './components/MovieList';

// Instead of defining a movies object in the App component, we fetch the movies object from a JSON file.
// We use the useEffect hook to fetch the movies object from the JSON file. It will be called only once when the component is mounted. As we are not passing any dependencies, it will not be called again. 

// We use the useState hook to define a state variable called movies and set it to an empty array. We then use the setMovies function to update the movies variable with the data fetched from the JSON file. Make sure to set a default value for the movies variable, otherwise you will get an error when the component is rendered for the first time.

function App() {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:3000/movies.json`)
            .then(res => res.json())
            .then(data => {
                setMovies(data.movies);
            });
    }, []);

    // Once the movies object is fetched, we pass it down to the MovieList component as a prop. We also define two functions that will be passed down to the MovieList component as props. The onMovieDelete function will be called when the delete button is clicked. The onMovieSelect function will be called when the select button is clicked.

    const onMovieDelete = (id) => {
        setMovies(state => state.filter(x => x.id !== id));
    };

    const onMovieSelect = (id) => {
        // We use the map function to set the selected property of the movie object to true if the id of the movie object matches the id passed to the onMovieSelect function. Otherwise, we set the selected property to false.
        setMovies(state => state.map(x => ({ ...x, selected: x.id === id })));
    };

    return (
        <div>
            <h1>Movie Collection</h1>

            <MovieList movies={movies} onMovieDelete={onMovieDelete} onMovieSelect={onMovieSelect} />
        </div>
    );
}

export default App;
