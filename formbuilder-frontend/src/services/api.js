import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  });

// Authentication
export const login = async (username, password) => {
    const response = await axios.post('/api/auth/login/', { 
        username, 
        password, 
    });
    localStorage.setItem('token',response.data.token);
};

// Forms
export const getForms = () => api.get('/forms/');
export const createForm = async (formData) => 
{
    const response = await api.post('/forms/', formData);
    return response.data;
}
// Fields
export const getFields = (formId) => api.get(`/forms/${formId}/fields/`);
export const createField = (data) => api.post('/fields/', data);

// Submit Form
export const submitForm = (formId, responses) => {
  api.post(`/forms/${formId}/submit/`, { 
    responses: [
        { field: 1, value: 'John Doe' },
        { field: 2, value: 'johndoe@example.com' },
      ],
    })
    .then(response => {
      alert('Form submitted successfully!');
    })
    .catch(error => {
      console.error('Submission failed:', error); 
    });
};