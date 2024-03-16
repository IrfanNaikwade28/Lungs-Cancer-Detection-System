var anchorTags = document.querySelectorAll(".dData");
var cardData = [
    {
        name: "Atelectasis | Standard value : 0.63",
        currentData : "{{data1}}",
        definition: "Atelectasis is a condition where part or all of a lung collapses.",
        symtoms: "Shortness of breath, rapid breathing, chest pain, coughing",
        careSteps: "Treatment involves deep breathing exercises, coughing exercises, incentive spirometry, and sometimes bronchodilators or suctioning to clear mucus from the airways."
    },
    {
        name: "Cardiomegaly | Standard value : 0.64",
        currentData : "{{data2}}",
        definition: "Cardiomegaly refers to an enlarged heart.Patients should focus on lifestyle modifications such as maintaining a healthy diet, regular exercise, managing stress, and adhering to prescribed medications to manage underlying conditions like high blood pressure or heart disease.",
        symtoms: "Shortness of breath, chest pain, cough, fever",
        careSteps: "Management includes medications to control blood pressure and heart rate, lifestyle changes such as a heart-healthy diet, exercise, and in severe cases, surgical interventions like valve repair or replacement."
    },
    {
        name: "Consolidation | Standard value : 0.68",
        currentData : "{{data3}}",
        definition: "Consolidation occurs when the airspaces in the lungs fill with fluid.It's important for patients to understand the importance of completing antibiotic courses if prescribed, staying hydrated, and getting plenty of rest. In severe cases, hospitalization may be necessary.",
        symtoms: "Symptoms: Shortness of breath, fatigue, swelling in the legs and ankles, irregular heartbeat.",
        careSteps: "Management includes medications to control blood pressure and heart rate, lifestyle changes such as a heart-healthy diet, exercise, and in severe cases, surgical interventions like valve repair or replacement."
    },
    {
        name: "Edema | Standard value : 0.74",
        currentData : "{{data4}}",
        definition: "Edema is swelling caused by excess fluid trapped in body tissues.Patients should monitor their salt intake, elevate affected limbs, wear compression garments if appropriate, and adhere to prescribed medications such as diuretics as directed by their healthcare provider.",
        symtoms: "Swelling in the feet, ankles, or legs, puffiness or swelling of the face, abdomen or other areas.",
        careSteps: "Management includes addressing the underlying cause, such as heart failure or kidney disease, through medications, dietary changes (like reducing salt intake), compression stockings, and elevating the affected limbs."
    },
    {
        name: "Effusion | Standard value : 0.70",
        currentData : "{{data5}}",
        definition: "Effusion refers to an abnormal accumulation of fluid in a body cavity, often seen in the lungs or abdomen.Understanding the underlying cause of the effusion is important for appropriate management. Treatment may include draining the fluid, treating the underlying condition, or both.",
        symtoms: "Shortness of breath, chest pain, cough, fever (if infected).",
        careSteps: "Treatment depends on the cause; it may include draining the fluid through procedures like thoracentesis or paracentesis, medications to reduce inflammation or fight infection, or addressing the underlying condition causing the effusion."
    },
    {
        name: "Emphysema | Standard value : 0.60",
        currentData : "{{data6}}",
        definition: "Emphysema is a type of chronic obstructive pulmonary disease (COPD) characterized by damage to the air sacs in the lungs.Smoking cessation is crucial to slow down the progression of emphysema. Patients should also focus on maintaining good nutrition, staying active within their limits, and using inhalers or other medications as prescribed.",
        symtoms: "Shortness of breath, wheezing, chronic cough, chest tightness.",
        careSteps: "Management involves quitting smoking, avoiding exposure to lung irritants, pulmonary rehabilitation, medications (such as bronchodilators and inhaled steroids), and in severe cases, supplemental oxygen therapy or surgery."
    },
    {
        name: "Fibrosis | Standard value : 0.61",
        currentData : "{{data7}}",
        definition: "Fibrosis involves the thickening and scarring of connective tissue, often seen in the lungs.Patients should understand the importance of avoiding exposure to environmental toxins, managing underlying conditions, and participating in pulmonary rehabilitation programs to maintain lung function.",
        symtoms: "Shortness of breath, dry cough, fatigue, unexplained weight loss.",
        careSteps: "Treatment may include medications to reduce inflammation and suppress the immune system, supplemental oxygen therapy, pulmonary rehabilitation, and in advanced cases, lung transplantation."
    },
    {
        name: "Hernia | Standard value : 0.65",
        currentData : "{{data8}}",
        definition: "A hernia occurs when an organ pushes through an opening in the muscle or tissue that holds it in place.Treatment may involve lifestyle changes such as weight loss, avoiding heavy lifting, and wearing supportive garments. In some cases, surgical intervention may be necessary.",
        symtoms: "Visible bulge in the affected area, pain or discomfort, especially when lifting or bending over.",
        careSteps: "Treatment involves surgery to repair the hernia, particularly if it is causing pain or complications like bowel obstruction."
    },
    {
        name: "Infiltration | Standard value : 0.61",
        currentData : "{{data9}}",
        definition: "Infiltration refers to the abnormal accumulation of substances such as cells, fluids, or foreign bodies within tissues or organs.Treatment depends on the underlying cause of the infiltration. Patients should follow their healthcare provider's recommendations closely, which may include medication, drainage procedures, or monitoring for resolution.",
        symtoms: "Fever, chills, cough, chest pain.",
        careSteps: "Management involves identifying and treating the underlying cause, which may include antibiotics for bacterial infections, antifungal medications for fungal infections, or supportive care for non-infectious causes."
    },
    {
        name: "Mass | Standard value : 0.61",
        currentData : "{{data10}}",
        definition: "A mass refers to a lump or growth of tissue that may be benign or malignant.Prompt evaluation by a healthcare provider is essential to determine the nature of the mass and appropriate treatment. This may involve imaging tests, biopsies, or surgical removal.",
        symtoms: "Can vary depending on the location and nature of the mass, but may include pain, swelling, changes in bowel or bladder habits, unexplained weight loss.",
        careSteps: "Treatment depends on the nature of the mass; it may involve surgical removal, chemotherapy, radiation therapy, or a combination of these treatments."
    },
    {
        name: "Nodule | Standard value : 0.55",
        currentData : "{{data11}}",
        definition: "A nodule is a small, abnormal growth or lump.Depending on the location and characteristics of the nodule, treatment may include monitoring for changes over time, further imaging or biopsy, or surgical removal.",
        symtoms: "Often asymptomatic but may cause coughing, wheezing, shortness of breath if pressing on nearby structures.",
        careSteps: "Management depends on the underlying cause and characteristics of the nodule; it may include observation, biopsy, or surgical removal."
    },
    {
        name: "Pleural Thickening | Standard value : 0.60",
        currentData : "{{data12}}",
        definition: "Pleural thickening involves the thickening and scarring of the pleura, the membrane that surrounds the lungs.Treatment may focus on managing underlying causes such as asbestos exposure or previous infections. In some cases, symptomatic relief with pain management may be necessary.",
        symtoms: "Shortness of breath, chest pain, persistent cough.",
        careSteps: "Treatment may involve addressing the underlying cause, such as asbestos exposure, and managing symptoms with pain relief medications, respiratory support, or surgical interventions in severe cases."
    },
    {
        name: "Pneumonia | Standard value : 0.63",
        currentData : "{{data13}}",
        definition: "Pneumonia is an infection that inflames the air sacs in one or both lungs.Patients should complete the full course of prescribed antibiotics, stay hydrated, get plenty of rest, and follow up with their healthcare provider as needed for monitoring.",
        symtoms: "Fever, cough, shortness of breath, chest pain, fatigue.",
        careSteps: "Treatment typically involves antibiotics for bacterial pneumonia, antiviral medications for viral pneumonia, rest, adequate hydration, and sometimes supplemental oxygen or hospitalization for severe cases."
    },
    {
        name: "Pneumothorax | Standard value : 0.62",
        currentData : "{{data14}}",
        definition: "Pneumothorax occurs when air leaks into the space between the lungs and the chest wall, causing the lung to collapse partially or fully.Depending on the severity, treatment may involve rest and observation, needle aspiration to remove air",
        symtoms: "Sudden sharp chest pain, shortness of breath, rapid heart rate, cyanosis (bluish discoloration of the skin).",
        careSteps: "Treatment usually involves chest tube insertion to remove air from the pleural space, allowing the lung to re-expand, along with pain management and monitoring for complications like tension pneumothorax. In some cases, surgery may be necessary to prevent recurrence."
    }
];

anchorTags.forEach(function(anchorTag) {
    anchorTag.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default anchor behavior

        // Get the index value from the anchor tag's value attribute
        var index = parseInt(anchorTag.getAttribute("value")) - 1;

        // Check if the index is valid
        if (index >= 0 && index < cardData.length) {
            // Update the content of the card with the data from cardData
            document.getElementById("diseaseName").textContent = cardData[index].name;
            document.getElementById("currentValue").textContent = cardData[index].currentData;
            document.getElementById("diseaseDefinition").textContent = cardData[index].definition;
            document.getElementById("diseaseSymptoms").textContent = cardData[index].symtoms;
            document.getElementById("diseaseCareSteps").textContent = cardData[index].careSteps;
            location.href = "#disease";
        } else {
            console.error("Invalid index:", index);
        }
    });
});
document.getElementById("learnMore").addEventListener("click",function(){
    location.href = "https://ijsrem.com/download/lung-cancer-detection-using-weakly-supervised-learning-for-leveraging-the-chestx-ray8-dataset-for-automated-classification/";
});