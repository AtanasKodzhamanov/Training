import React, { useState } from "react";
// React hook, it's a function that starts with "use" and it allows us to use state in functional components
import ExpenseDate from "./ExpenseDate";
import Card from "../UI/Card";
import "./ExpenseItem.css";

const ExpenseItem = (props) => {
  // hooks should be used in the root of the component function
  // useState() returns an array with 2 elements
  // Naming convention:
  // 1st element: the name of the state snapshot
  // 2nd element: the name of the function that allows us to update the state
  const [title, setTitle] = useState(props.title);

  const clickHandler = () => {
    setTitle("Updated!"); // this will update the state and re-render the component with the new state
    console.log(title);
  };

  return (
    <Card className="expense-item">
      <ExpenseDate date={props.date} />
      <div className="expense-item__description">
        <h2>{title}</h2>
        <div className="expense-item__price">${props.amount}</div>
      </div>
      <button onClick={clickHandler}>Change Title</button>
    </Card>
  );
};

export default ExpenseItem;
