import React from "react";
import { useSelector } from "react-redux";
import TodoCounterComponent from "./TodoCounterComponent.js";

function TodoCounterContainer() {
    const { completed, uncompleted } = useSelector(
        (state) => state.todoReducer
    );

    return (
        <TodoCounterComponent completed={completed} uncompleted={uncompleted} />
    );
}

export default TodoCounterContainer;
