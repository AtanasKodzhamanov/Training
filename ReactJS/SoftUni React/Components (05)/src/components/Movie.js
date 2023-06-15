import { useEffect } from "react";
import styles from './Movie.module.css';

// we deconstruct the props object and get the properties we need
export default function Movie({
    id,
    title,
    year,
    plot,
    posterUrl,
    director,
    onMovieDelete,
    onMovieSelect,
    selected,
}) {
    // whenever the component is mounted, title updated or unmounted, the useEffect hook will be called
    useEffect(() => {
        console.log(`Movie ${title} - mounted!`);

        return () => {
            console.log(`Movie ${title} - unmounted!`);
        }
    }, [title]);

    // whenever the component title is updated or component selected, the useEffect hook will be called
    useEffect(() => {
        console.log(`Movie ${title} - updated!`);
    }, [selected, title]);

    return (
        <article className={styles['movie-article']}>
            <h3>{title}, {year}</h3>
            {selected && <h4>Selected</h4>}
            <main>
                <img src={posterUrl} alt={title} />
                <p>{plot}</p>
            </main>
            <footer>
                <p>director: {director}</p>
                <button onClick={() => onMovieDelete(id)}>Delete</button>
                <button onClick={() => onMovieSelect(id)}>Select</button>
            </footer>
        </article>
    );
};