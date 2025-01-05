import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { createField, api } from '../services/api';
import { Button, TextField, MenuItem } from '@mui/material';

const fieldTypes = [
  { label: 'Text', value: 'text' },
  { label: 'Number', value: 'number' },
  { label: 'Date', value: 'date' },
];

const FormBuilder = ({ formId }) => {
  const [fields, setFields] = useState([]);

  const handleDragEnd = (result) => {
    if (!result.destination) return;
    const items = Array.from(fields);
    const [movedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, movedItem);
    setFields(items);
    items.forEach((field, index) => {
        api.patch(`/fields/${field.id}/`, { order: index + 1 });
      });
  };

  const addField = () => {
    setFields([...fields, { label: '', field_type: 'text', required: false }]);
  };

  const handleFieldChange = (index, field) => {
    const updatedFields = [...fields];
    updatedFields[index] = field;
    setFields(updatedFields);
  };

  const saveFields = () => {
    fields.forEach((field, index) => {
      createField({
        form: formId,
        label: field.label,
        field_type: field.field_type,
        required: field.required,
        order: index + 1,
      });
    });
  };

  return (
    <div>
      <h2>Form Builder</h2>
      <Button onClick={addField}>Add Field</Button>
      <DragDropContext onDragEnd={handleDragEnd}>
        <Droppable droppableId="fields">
          {(provided) => (
            <div {...provided.droppableProps} ref={provided.innerRef}>
              {fields.map((field, index) => (
                <Draggable
                  key={index}
                  draggableId={`field-${index}`}
                  index={index}
                >
                  {(provided) => (
                    <div
                      ref={provided.innerRef}
                      {...provided.draggableProps}
                      {...provided.dragHandleProps}
                    >
                      <TextField
                        label="Field Label"
                        value={field.label}
                        onChange={(e) =>
                          handleFieldChange(index, {
                            ...field,
                            label: e.target.value,
                          })
                        }
                        fullWidth
                        margin="dense"
                      />
                      <TextField
                        select
                        label="Field Type"
                        value={field.field_type}
                        onChange={(e) =>
                          handleFieldChange(index, {
                            ...field,
                            field_type: e.target.value,
                          })
                        }
                        fullWidth
                        margin="dense"
                      >
                        {fieldTypes.map((type) => (
                          <MenuItem key={type.value} value={type.value}>
                            {type.label}
                          </MenuItem>
                        ))}
                      </TextField>
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}
        </Droppable>
      </DragDropContext>
      <Button onClick={saveFields} variant="contained" color="primary">
        Save Form
      </Button>
    </div>
  );
};

export default FormBuilder;
