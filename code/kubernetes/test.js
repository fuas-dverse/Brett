import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '10s',
  cloud: {
    // Project: Default project
    // Test runs with the same name groups test runs together.
    name: 'Test (26/04/2024-10:29:12)'
  }
};

export default function() {
  http.get('http://localhost:5001/');
  sleep(0.0001);
}