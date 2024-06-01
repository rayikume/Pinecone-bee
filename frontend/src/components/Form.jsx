import axios from "axios";
import React from "react";
import { useState } from "react";

const Form = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:8000", { prompt: inputValue })
      .then((res) => {
        console.log(res.data);
        window.location.reload();
      })
      .catch((err) => {
        console.error("Error submitting form: ", err);
      });
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
