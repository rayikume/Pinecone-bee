import React from "react";
import { useState } from "react";

const Form = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const question = { question: inputValue };

    fetch("http://localhost:5000/models/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(question),
    }).then(console.log(JSON.stringify(question)));
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
