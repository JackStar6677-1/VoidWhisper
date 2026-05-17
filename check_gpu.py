import torch

print("=" * 60)
print("CUDA / GPU CHECK")
print("=" * 60)
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA device count: {torch.cuda.device_count()}")

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")
        props = torch.cuda.get_device_properties(i)
        gb = props.total_memory / 1024 / 1024 / 1024
        print(f"  Memory: {gb:.2f} GB")
else:
    print("NO GPU DETECTED")
print("=" * 60)
