import dotenv from 'dotenv';
import express from 'express';

dotenv.config();

const app = express();

const port = process.env.PORT || 5000;

app.listen(port, () => {
  console.log(`server connected on port ${port}`);
});