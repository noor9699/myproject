import React from "react";

const Button = ({link, name, title}) => {
  return (
    <>
      <a href={link} className={name}>
        {title}
      </a>
    </>
  );
};

export default Button;
