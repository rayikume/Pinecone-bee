import React from "react";
import { useState, useEffect, useContext } from "react";
import io from "socket.io-client";
import { LoadingContext } from "../context/context";
import { circlesLoop } from "../assets/assets";

const socket = io("http://localhost:5000");

export const Models = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useContext(LoadingContext);

  useEffect(() => {
    socket.on("response", (data) => {
      setData(data);
      setLoading(false);
    });

    return () => {
      socket.off("connect");
      socket.off("message");
    };
  }, []);

  return (
    <section>
      {loading ? (
        <img src={circlesLoop} className="loading" />
      ) : data ? (
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
      ) : (
        <div></div>
      )}
    </section>
  );
};

export default Models;
