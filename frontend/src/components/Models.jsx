import React from "react";
import { useState, useEffect } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000");

export const Models = () => {
  const [data, setData] = useState(null);

  // useEffect(() => {
  //   fetch("http://127.0.0.1:5000/models/", {
  //     method: "GET",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //   })
  //     .then((res) => {
  //       return res.json();
  //     })
  //     .then((data) => {
  //       setData(data);
  //     });
  // }, []);

  useEffect(() => {
    socket.on("response", (data) => {
      setData(data);
    });

    return () => {
      socket.off("connect");
      socket.off("message");
    };
  }, []);

  return (
    <>
      <div className="flex flex-row gap-5 m-10">
        <div className="summary_box .gradient-border">
          <h1 className="font-satoshi font-bold text-xl orange_gradient">
            ✦ ChatGPT-3 Turbo
          </h1>
          <br />
          <p className="font-inter font-medium text-sm text-white">
            {data && data["ChatGPT3"] ? data["ChatGPT3"] : ""}
          </p>
        </div>
        <div className="summary_box .gradient-border">
          <h1 className="font-satoshi font-bold text-xl orange_gradient">
            ✦ ChatGPT-4
          </h1>
          <br />
          <p className="font-inter font-medium text-sm text-white">
            {data && data["ChatGPT4"] ? data["ChatGPT4"] : ""}
          </p>
        </div>
        <div className="summary_box .gradient-border">
          <h1 className="font-satoshi font-bold text-xl orange_gradient">
            ✦ Llama Chat
          </h1>
          <br />
          <p className="font-inter font-medium text-sm text-white">
            {data && data["llama"] ? data["llama"] : ""}
          </p>
        </div>
      </div>
    </>
  );
};

export default Models;
