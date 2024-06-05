import React, { useContext, useEffect } from "react";
import { useState } from "react";
import io from "socket.io-client";
import { LoadingContext } from "../context/context";

const socket = io("http://localhost:5000");

const Form = () => {
  const [inputValue, setInputValue] = useState("");
  const [loading, setLoading] = useContext(LoadingContext);

  useEffect(() => {
    socket.on("connect", () => {
      console.log("Connected to server");
    });

    return () => {
      socket.off("connect");
      socket.off("message");
    };
  }, []);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (inputValue) {
      socket.emit("message", inputValue);
      setInputValue("");
      setLoading(true);
    }
  };

  return (
    <section className="mt-16 w-full max-w-xl">
      <div className="flex flex-col w-full gap-2">
        <form
          onSubmit={handleSubmit}
          method="post"
          className="relative flex justify-center items-center"
        >
          <input
            className="url_input peer"
            placeholder="Enter a prompt"
            value={inputValue}
            onChange={handleInputChange}
          ></input>
          <button type="submit" className="submit_btn text-gray-100">
            Submit
          </button>
        </form>
      </div>
    </section>
  );
};

export default Form;
