import React from "react";
import { Card } from "antd";
const { Meta } = Card;

const ProblemCard = ({ path, title, description }) => (
  <Card
    hoverable
    style={{ width: 340, margin: "1rem" }}
    cover={
      <div
        style={{
          height: "120px",
          overflow: "hidden",
          position: "relative",
          background: "#001529"
        }}
      >
        <img
          alt="example"
          style={{
            width: "100%",
            position: "absolute",
            top: "50%",
            transform: "translateY(-50%)"
          }}
          src={path}
        />
      </div>
    }
  >
    <Meta title={title} description={description} />
  </Card>
);

export default ProblemCard;
