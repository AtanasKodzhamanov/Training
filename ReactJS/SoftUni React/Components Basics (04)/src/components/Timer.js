import { useState } from 'react';

// example of state management
// We define a state variable called seconds and set it to the value of the start prop. 
// We then use the setSeconds function to update the seconds variable by adding 1 to it every second.
// Then we display the seconds variable in the JSX.
const Timer = (props) => {
    const [seconds, setSeconds] = useState(props.start);

    // Not good practice (useEffect is better)
    setTimeout(() => {
        setSeconds(state => state + 1);
    }, 1000);

    return (
        <div>
            <h2>Timer</h2>
            Time: {seconds}s
        </div>
    );
};

export default Timer;