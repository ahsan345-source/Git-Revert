# 🚀 System & Performance Tracker Test
print("--- 🛠️ DevOps Quick System Script ---")

# User & Role Check
username = input("Apna Username darj karein: ")
role = input("Aapka Role kya hai? (Dev / Ops / Student): ").strip().lower()

print(f"\nAccess Granted: Welcome to the profile , {username}!")

if role in ["dev", "ops", "devops"]:
    print("⚡ Status: Admin / Infrastructure Access Active!")
else:
    print("👤 Status: Standard User / Student Mode Active!")
print("\n--- 📊 Memory Usage Calculator ---")
try:
    total_ram = float(input("Total System RAM (GBs me): "))
    used_ram = float(input("Used System RAM (GBs me): "))
    
    free_ram = total_ram - used_ram
    usage_percentage = (used_ram / total_ram) * 100
    
    print(f"\n💾 ypur free ram is : {free_ram:.2f} GB")
    print(f"📈 Memory Load: {usage_percentage:.1f}%")
    
    if usage_percentage > 80:
        print("⚠️ WARNING: High Memory Usage!")
    else:
        print("✅ System Health Normal.")

except ValueError:
    print("❌ Error: Baraye meherbani sirf numbers (digits) darj karein!")