import React from "react";
import { Layout } from "antd";
import { Content } from "./component";

const {Content: ContentFromAntd } = Layout;
function App() {
  return (
    <Layout className="app">
      {/* <Header>
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={["2"]}>
          <Menu.Item key="1">nav 1</Menu.Item>
          <Menu.Item key="2">nav 2</Menu.Item>
          <Menu.Item key="3">nav 3</Menu.Item>
        </Menu>
      </Header> */}
      <ContentFromAntd className="Content">
        <Content />


      </ContentFromAntd>
      <input type='file'/>
    </Layout>
  );
}

export default App;
