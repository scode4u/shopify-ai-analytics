class PythonClient
  include HTTParty
  base_uri "http://localhost:8000"

  def self.ask(payload)
    post("/ask", body: payload.to_json, headers: { "Content-Type" => "application/json" })
  end
end
