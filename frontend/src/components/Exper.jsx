import React, { useState, useEffect } from "react";
import axios from "axios";

const Exper = () => {
  const [prompte, setPrompte] = useState({ details: [] });

  useEffect(() => {
    axios
      .get("http://localhost:8000")
      .then((res) => {
        setPrompte({ details: res.data });
      })
      .catch((err) => {
        console.log(err);
      });
  }, []); // Empty dependency array means this effect runs once after the first render

  return (
    <div>
      {prompte.details.map((output, id) => (
        <div key={id}>
          <div>{output.prompt}</div>
        </div>
      ))}
    </div>
  );
};

export default Exper;
