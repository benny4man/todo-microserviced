import React from "react";
import LoadingOverlayComponent from "./LoadingOverlayComponent.js";
import { useSelector } from "react-redux";

function LoadingOverlayContainer() {
    const { isFetching } = useSelector((state) => state.todoReducer);

    return <LoadingOverlayComponent active={isFetching} />;
}

export default LoadingOverlayContainer;
