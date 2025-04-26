import React from "react";
import ClearCompletedButtonComponent from "./ClearCompletedButtonComponent.js";
import { useDispatch, useSelector } from "react-redux";
import { fetchClearCompletedTodoItem } from "../../actions/todoAction.js";

function ClearCompletedButtonContainer() {
    const dispatch = useDispatch();
    const { isLoggedIn } = useSelector((state) => state.authReducer);

    function onClickClearCompletedButton() {
        dispatch(fetchClearCompletedTodoItem());
    }

    return (
        <ClearCompletedButtonComponent
            isLoggedIn={isLoggedIn}
            onClick={onClickClearCompletedButton}
        />
    );
}

export default ClearCompletedButtonContainer;
