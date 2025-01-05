import React, { useEffect, useState } from 'react';
import { getForms } from '../services/api';

const FormList = () => {
  const [forms, setForms] = useState([]);

  useEffect(() => {
    getForms().then((response) => {
      setForms(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Forms</h2>
      {forms.map((form) => (
        <div key={form.id}>
          <h3>{form.title}</h3>
          <p>{form.description}</p>
        </div>
      ))}
    </div>
  );
};

export default FormList;
