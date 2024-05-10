import React from "react";

const Card = () => {
  // const { value, name, img } = link;
  const CardData = [
    {
      value: "1839",
      name: "Days on the market",
      img: "stats__dodger--purple",
    },
    {
      value: "5812",
      name: "Members",
      img: "stats__dodger--orange",
    },
    {
      value: "$374 103",
      name: "Arbitrage pools",
      img: "stats__dodger--green",
    },
    {
      value: "$100 812",
      name: "Total paid",
      img: "stats__dodger--red",
    },
  ];
  return (
    <>
      {/* <!-- statistics --> */}
      <div className="section">
        <div className="container">
          <div className="row">
            {CardData.map((link, index) => (
              <div className="col-12 col-sm-6 col-xl-3">
                {/* <!-- stats --> */}
                <div class="stats">
                  <span class="stats__value">{link.value}</span>
                  <p class="stats__name">{link.name}</p>

                  {/* <!-- design elements --> */}
                  <span
                    class={`stats__dodger stats__dodger--left  ${link.img}`}
                  ></span>
                  <span
                    class={`stats__dodger stats__dodger--right  ${link.img}`}
                  ></span>
                </div>
                {/* <!-- end stats --> */}
              </div>
            ))}
            ;
          </div>
        </div>
      </div>
      {/* <!--End statistics --> */}
    </>
  );
};
export default Card;
