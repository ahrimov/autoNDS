import React, { useState } from 'react';
import axios from 'axios';

export function UploadPDF() {
    const [file, setFile] = useState(null);

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8000/api/documents/',
                formData,
                { headers: { 'Content-Type': 'multipart/form-data' }}
            );
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <input 
                type="file" 
                onChange={(e) => setFile(e.target.files[0])} 
            />
            <button onClick={handleUpload}>Загрузить</button>
        </div>
    );
}