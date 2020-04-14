import React from "react";
import { Card } from "antd";
const { Meta } = Card;

const ProblemCard = ({ path, title, description }) => (
  <Card
    hoverable
    style={{ width: 240 }}
    cover={<img alt="example" src={path} />}
  >
    <Meta title={title} description={description} />
  </Card>
);

export default ProblemCard;
