import openai

def finetune_model(
    training_file_id: str,
    model: str = "gpt-4o",
    n_epochs: int = 10,
    batch_size: int = 1,
    learning_rate_multiplier: int = 2,
) -> dict:
    """
    Create a fine-tuning job with essential parameters only.
    """
    params = {
        "training_file": training_file_id,
        "model": model,
        "hyperparameters": {
            "n_epochs": n_epochs,
            "batch_size": batch_size,
            "learning_rate_multiplier": learning_rate_multiplier,
        }
    }
    
    try:
        response = openai.FineTuningJob.create(**params)
        return response
    except Exception as e:
        print(f"Error creating fine-tuning job: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    openai.api_key = "your-api-key-here"
    
    result = finetune_model(
        training_file_id="your-training-file-id",
        model="gpt-4o",
        n_epochs=10,
        batch_size=1,
        learning_rate_multiplier=1
    )
    
    if result:
        print("Fine-tuning job created successfully!")
        print(f"Job ID: {result.id}")
