import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchTodoList } from "../../actions/todoAction.js";
import { getDisplayTodos } from "../../utils/getDisplayTodos.js";
import TodoListComponent from "./TodoListComponent.js";
import Cookies from "universal-cookie";

const cookies = new Cookies();

function TodoListContainer() {
    const dispatch = useDispatch();
    const { isLoggedIn } = useSelector((state) => state.authReducer);
    const { todos } = getDisplayTodos(
        useSelector((state) => state.todoReducer),
        useSelector((state) => state.todoDisplayFilterReducer)
    );

    useEffect(() => {
        function getAccessToken() {
            return cookies.get("Access-Token");
        }

        if (isLoggedIn || getAccessToken()) {
            dispatch(fetchTodoList());
        }
    }, [dispatch, isLoggedIn]);

    return <TodoListComponent todos={todos} isLoggedIn={isLoggedIn} />;
}

export default TodoListContainer;
