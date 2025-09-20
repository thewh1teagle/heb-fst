use anyhow::Result;
use rustfst::prelude::*;
use rustfst::algorithms::compose::compose;
use std::path::Path;
use std::time::{Duration, Instant};

fn main() -> Result<()> {
    let input = "יָאִיר";
    let expected_output = "ʃalˈom";
    let fst_path = "hebrew_phonemizer.fst";
    
    // Check if FST file exists
    if !Path::new(fst_path).exists() {
        println!("FST file not found: {}", fst_path);
        return Ok(());
    }
    
    // Load the FST
    let phonemizer_fst: VectorFst<TropicalWeight> = VectorFst::read(fst_path)?;
    
    // Phonemize the input
    let result = phonemize_string(input, &phonemizer_fst)?;
    
    match result {
        Some(output) => {
            println!("Input: {}", input);
            println!("Output: {}", output);
            
            if output == expected_output {
                println!("✓ Success! Output matches expected result.");
            } else {
                println!("✗ Output doesn't match expected result.");
                println!("Expected: {}", expected_output);
            }
        }
        None => {
            println!("✗ No phonemization found for input: {}", input);
        }
    }
    
    // Performance benchmark - run for 1 second
    println!("\n--- Performance Benchmark ---");
    println!("Running phonemizer for 1 second...");
    
    let start_time = Instant::now();
    let duration = Duration::from_secs(1);
    let mut count = 0;
    
    while start_time.elapsed() < duration {
        if let Some(_) = phonemize_string(input, &phonemizer_fst)? {
            count += 1;
        }
    }
    
    let elapsed = start_time.elapsed();
    let words_per_sec = count as f64 / elapsed.as_secs_f64();
    
    println!("Processed {} words in {:.2}s", count, elapsed.as_secs_f64());
    println!("Performance: {:.0} words per second", words_per_sec);
    
    Ok(())
}

fn create_string_acceptor(input: &str) -> Result<VectorFst<TropicalWeight>> {
    let mut fst = VectorFst::<TropicalWeight>::new();
    
    let mut current_state = fst.add_state();
    fst.set_start(current_state)?;
    
    // Convert string to UTF-8 bytes (FST uses byte encoding)
    for byte in input.bytes() {
        let next_state = fst.add_state();
        let label = byte as u32;
        fst.add_tr(current_state, Tr::new(label, label, TropicalWeight::one(), next_state))?;
        current_state = next_state;
    }
    
    fst.set_final(current_state, TropicalWeight::one())?;
    Ok(fst)
}

fn phonemize_string(input: &str, phonemizer_fst: &VectorFst<TropicalWeight>) -> Result<Option<String>> {
    // Create input acceptor and compose with phonemizer FST
    let input_fst = create_string_acceptor(input)?;
    let composed: VectorFst<TropicalWeight> = compose::<TropicalWeight, VectorFst<TropicalWeight>, VectorFst<TropicalWeight>, VectorFst<TropicalWeight>, _, _>(&input_fst, phonemizer_fst)?;
    
    if composed.num_states() == 0 {
        return Ok(None);
    }
    
    // Extract output string from first valid path
    for path in composed.paths_iter() {
        let output_bytes: Vec<u8> = path.olabels.iter()
            .filter_map(|&label| if label != 0 && label <= 255 { Some(label as u8) } else { None })
            .collect();
            
        if !output_bytes.is_empty() {
            if let Ok(output_string) = String::from_utf8(output_bytes) {
                return Ok(Some(output_string));
            }
        }
    }
    
    Ok(None)
}