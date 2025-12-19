class Api::V1::QuestionsController < ApplicationController
  def create
    return render json: { error: "Invalid input" }, status: 400 unless params[:question]

    response = PythonClient.ask(
      store_id: params[:store_id],
      question: params[:question]
    )

    render json: response
  end
end
