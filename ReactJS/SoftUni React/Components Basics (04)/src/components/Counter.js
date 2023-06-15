import { useState } from "react";
// Example of state management and functions
// We define a state variable called counter and set it to the value of 0.
// We then use the setCounter function to update the counter variable by adding 1 to it every time the incrementCounterHanlder function is called.
// Then we display the counter variable in the JSX.
// We also define a decrementCounterHandler function that subtracts 1 from the counter variable every time it is called.
// We also define a clearCounterHanlder function that sets the counter variable to 0 every time it is called.
// We also define a getTitle function that returns a string based on the value of the counter variable.

const getTitle = (count) => {
    switch (count) {
        case 1:
            return 'First Blood';
        case 2:
            return 'Double Kill';
        case 3:
            return 'Tripple Kill';
        case 4:
            return 'Multi Kill';
        case 5:
            return 'Unstoppable';
        default:
            return 'Counter';
    }
};

const Counter = (props) => {
    const [counter, setCounter] = useState(0);

    const incrementCounterHanlder = () => {
        setCounter(oldCounter => oldCounter + 1);
    };

    const decrementCounterHandler = () => {
        setCounter(oldCounter => oldCounter - 1);
    };

    const clearCounterHanlder = () => {
        setCounter(0);
    };

    return (
        <div>
            <p style={{ fontSize: Math.max(counter, 1) / 2 + 'em' }}>
                {counter > 5 ? 'Godlike' : getTitle(counter)}: {counter}
            </p>

            <button onClick={decrementCounterHandler}>-</button>

            {props.canReset && <button onClick={clearCounterHanlder}>0</button>}

            {counter < 10
                ? <button onClick={incrementCounterHanlder}>+</button>
                : null
            }
        </div>
    );
};

export default Counter;