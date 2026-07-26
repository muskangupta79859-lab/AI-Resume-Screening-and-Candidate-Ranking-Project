from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_candidate_pdf(candidate):

    file_name = f"{candidate['Candidate']}_report.pdf"

    pdf = canvas.Canvas(
        file_name,
        pagesize=letter
    )


    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        150,
        750,
        "Candidate Evaluation Report"
    )


    pdf.setFont(
        "Helvetica",
        12
    )


    y = 700


    details = [

        f"Candidate Name : {candidate['Candidate']}",

        f"Match Score : {candidate['Match %']}%",

        f"Prediction : {candidate['Prediction']}",

        f"Matched Skills : {', '.join(candidate['Matched Skills'])}",

        f"Missing Skills : {', '.join(candidate['Missing Skills']) if candidate['Missing Skills'] else 'None'}"

    ]


    for detail in details:

        pdf.drawString(
            70,
            y,
            detail
        )

        y -= 40


    pdf.save()


    return file_name