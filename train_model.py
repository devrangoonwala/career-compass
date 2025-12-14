#!/usr/bin/env python3
"""
Training script using HuggingFace Transformers
Reads oumi_train.yaml configuration and trains the model
"""
import yaml
import os
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import load_dataset
from rich.console import Console

console = Console()

def load_config():
    """Load training configuration from YAML"""
    with open("oumi_train.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config

def prepare_dataset(config):
    """Load and prepare the dataset"""
    data_config = config["data"]["train"]["datasets"][0]
    dataset_path = data_config["dataset_path"]
    
    console.print(f"[info]Loading dataset from: {dataset_path}[/info]")
    
    # Load text dataset
    dataset = load_dataset("text", data_files=dataset_path, split="train")
    
    return dataset

def tokenize_dataset(dataset, tokenizer):
    """Tokenize the dataset"""
    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, max_length=128)
    
    tokenized = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
    return tokenized

def main():
    console.print("[info]Starting model training...[/info]")
    
    # Load configuration
    config = load_config()
    model_name = config["model"]["model_name"]
    output_dir = config["training"]["output_dir"]
    
    console.print(f"[info]Model: {model_name}[/info]")
    console.print(f"[info]Output directory: {output_dir}[/info]")
    
    # Load tokenizer and model
    console.print("[info]Loading tokenizer and model...[/info]")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
    
    # Add padding token if it doesn't exist
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    # Prepare dataset
    dataset = prepare_dataset(config)
    tokenized_dataset = tokenize_dataset(dataset, tokenizer)
    
    # Setup training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=config["training"]["num_train_epochs"],
        per_device_train_batch_size=config["training"]["per_device_train_batch_size"],
        learning_rate=config["training"]["learning_rate"],
        save_steps=config["training"]["save_steps"],
        dataloader_num_workers=config["training"]["dataloader_num_workers"],
        logging_steps=1,
        save_total_limit=3,
    )
    
    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,  # Causal LM, not masked LM
    )
    
    # Create trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )
    
    # Train
    console.print("[info]Starting training...[/info]")
    trainer.train()
    
    # Save model
    console.print("[info]Saving model...[/info]")
    trainer.save_model()
    tokenizer.save_pretrained(output_dir)
    
    console.print(f"[success]Training completed! Model saved to {output_dir}[/success]")

if __name__ == "__main__":
    main()

