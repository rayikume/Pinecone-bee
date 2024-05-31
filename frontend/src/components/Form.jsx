import React from "react";
import { useState } from "react";

const Form = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Input value: ${inputValue}`);
  };

  return (
    <section className="">
      <div className="">
        <form onSubmit={handleSubmit}>
          <input
            className="w-full"
            value={inputValue}
            onChange={handleInputChange}
          ></input>
          <button type="submit">Submit</button>
        </form>
      </div>
    </section>
  );
};

export default Form;
