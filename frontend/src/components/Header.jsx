import React from "react";

const Header = () => {
  return (
    <header className="w-full flex justify-center item-center flex-col">
      <nav className="flex justify-between items-center w-full mb-10 pt-3">
        <div className="font-satoshi font-bold text-white text-3xl">
          ✦ Pinecone Bee
        </div>
        <button
          type="button"
          onClick={() =>
            window.open("https://github.com/rayikume/Pinecone-bee")
          }
          className="black_btn font-satoshi font-bold"
        >
          Github
        </button>
      </nav>
      <h1 className="head_text font-satoshi">
        Get Any Info About UAE with <br className="max-md:hidden" />
        <span className="orange_gradient">OpenAI GPT-4 and Llama-Chat</span>
      </h1>
      <h2 className="desc font-satoshi">
        Get quick and accurate information about UAE culture and laws
        <br />
        Powered directly from the official UAE government website!
      </h2>
    </header>
  );
};

export default Header;
