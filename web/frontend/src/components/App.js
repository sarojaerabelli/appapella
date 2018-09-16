import React from "react";
import ReactDOM from "react-dom";
import Recorder from "./Recorder";

const App = () => (
    <Recorder />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;